from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from .forms import PostForm, briefForm,  rawBriefForm, assignForm, officerForm
from django.views.generic import DetailView
from django.db.models import Sum, Count, Avg, Q
from django.db.models.functions import ExtractYear,TruncYear

# Create your views here.

from .models import Briefs, Categories, Officers, Assignment

class AjaxTemplateMixin(object):
      def dispatch(self, request, *args, **kwargs):
          if not hasattr(self, 'ajax_template_name'):
             split = self.template_name.split('.htm')
             split[-1] = '_inner'
             split.append('.htm')
             self.ajax_template_name = ''.join(split)
          if request.is_ajax():
             self.template_name = self.ajax_template_name
          return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class IndexView(generic.ListView):
    template_name = 'pulse/index.htm'
    context_object_name = 'latest_brief_list'

    def get_queryset(self):
        return Briefs.objects.order_by('brief_id')[:15]

class DetailView(generic.DetailView):
    template_name = 'pulse/detail.htm'
    #category = get_object_or_404(Categories, pk=Categories.category_id)
    context_object_name = 'latest_category_details'

    def get_queryset(self):
        return Categories.objects.order_by('category_id')[:10]
        #return HttpResponse("You're voting on question %s." % 25255)

def officerDetailView(request, pk):
    id_ya_officer = pk
    officer = Officers.objects.get(officer_id=id_ya_officer)
    assign = Assignment.objects.order_by('-date').filter(officer=officer)
    content={
      'officer_details':officer,
      'pb_details':assign
    }
    return render(request = request, template_name = 'pulse/officerDetail.htm', context=content)

def pbDetailView(request, pk):
    id_ya_pb = pk
    pb = Briefs.objects.get(brief_id=id_ya_pb)
    assign = Assignment.objects.order_by('-date').filter(project=id_ya_pb)
    content={
      'pb_details':pb,
      'pbAss_details':assign
    }
    return render(request = request, template_name = 'pulse/pbDetail.htm', context=content)

def cssView(request):
    pb = Briefs.objects.order_by('brief_id')[:15]
    assign = Assignment.objects.order_by('-date')[:15]
    content={
      'pb_details':pb,
      'pbAss_details':assign
    }
    return render(request = request, template_name = 'pulse/css.htm', context=content)

def letterView(request, pk):
    id_ya_pb = pk
    pb = Briefs.objects.get(brief_id=id_ya_pb)
    assign = Assignment.objects.order_by('-date').filter(project=id_ya_pb)
    content={
      'pb_details':pb,
      'pbAss_details':assign
    }
    return render(request = request, template_name = 'pulse/letter.htm', context=content)

def commentView(request, pk):
    id_ya_pb = pk
    pb = Briefs.objects.get(brief_id=id_ya_pb)
    assign = Assignment.objects.order_by('-date').filter(project=id_ya_pb)
    content={
      'pb_details':pb,
      'pbAss_details':assign
    }
    return render(request = request, template_name = 'pulse/comment.htm', context=content)

def boardView(request, pk):
    id_ya_pb = pk
    pb = Briefs.objects.get(brief_id=id_ya_pb)
    assign = Assignment.objects.order_by('-date').filter(project=id_ya_pb)
    content={
      'pb_details':pb,
      'pbAss_details':assign
    }
    return render(request = request, template_name = 'pulse/boardView.htm', context=content)

def briefDetailView2(request, pk):
    id_ya_brief = pk
    brief = Briefs.objects.get(brief_id=id_ya_brief)    
    #brief = get_object_or_404(Briefs, pk=Briefs.brief_id)
    content={
      'brief_details':brief
    }
    return render(request = request, template_name = 'pulse/detail.htm', context=content)

def project_create_view(request):
    form = briefForm(request.POST or None)
    if form.is_valid():
       form.save()
       
    context = {
            'form': form
    }
    return render(request, "pulse/captureAcknowledgement.htm", context)


def project_create_view1(request):
    form2 = rawBriefForm(request.POST or None)
    if form2.is_valid():
       form2.save()
    else:
         print(form2.errors)
    context = {
            'form': form2
    }
    return render(request, "pulse/captureAcknowledgement.htm", context)

def project_edit_view(request):
    form2 = rawBriefForm(request.POST or None)
    if form2.is_valid():
       form2.save()
    else:
         print(form2.errors)
    context = {
            'form': form2
    }
    return render(request, "pulse/captureAcknowledgement.htm", context)

def assignPB(request):
    form = assignForm(request.POST or None)
    assignmentList = Assignment.objects.order_by('ass_id')
    if form.is_valid():
       form.save()
    else:
         print(form.errors)
    context = {
            'form': form,
            'assignment_list': assignmentList
    }
    return render(request, "pulse/assignPB.htm", context)

def addOfficer(request):
    form = officerForm(request.POST or None)
    officers = Officers.objects.order_by('officer_id')
    if form.is_valid():
       form.save()
    context = {
            'form': form,
            'officer_list': officers
    }
    return render(request, "pulse/addOfficer.htm", context)

def project_delete_view(request,id):
    obj = get_object_or_404(Briefs,brief_id=id)
    if request.method == "POST":  #instead of a DELETE request
       obj.delete()
       return redirect("../")
    context = {
            "object":obj
    }
    return render(request, "pulse/confirmDelete.htm", context)

def grouped(request):
  metrics =  {
      'sector': Count('brief_id'),
      #'avg_charged_amount': Sum('charged_amount'),
      'frequency': Count('sector2', distinct=True),
  }

 # results = (
 #     Sale.objects
  #    .values('merchant', 'device')
  #    .annotate(**metrics)
  #)
  bySector = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  byCategory = Briefs.objects.order_by('-frequency')[:20].values('category').annotate(frequency=Count('brief_id'))
  byDeveloper = Briefs.objects.order_by('-frequency')[:20].values('developer','sector').annotate(frequency=Count('brief_id'))
  #qs = Purchases.objects.annotate(year=ExtractYear('date')).filter(year = today.year)

  yearTrend2 = Briefs.objects.order_by('yearx')[:100].values('received').annotate(yearx=ExtractYear('received'))#.aggregate(Count('received'))

  #yearTrend = Briefs.objects.all()[:10].annotate(yearx=TruncYear('received')).values('yearx').annotate(frequency=Count('brief_id'))                                                                                                          #, distinct=True
  #yearTrend = Briefs.objects.order_by('yearx').annotate(yearx=TruncYear('received')).values('yearx').annotate(frequency=Count('brief_id'))                                                                                                    #, distinct=True
  yearTrend = Briefs.objects.order_by('yearx').annotate(yearx=ExtractYear('received')).values('yearx').annotate(frequency=Count('brief_id'))                                                                                                          #, distinct=True

  #yearTrend = Briefs.objects.order_by('received')[:10].values('received').annotate(frequency=Count(ExtractYear('received')))
  byLocation = Briefs.objects.order_by('-frequency')[:20].values('locationx').annotate(frequency=Count('brief_id'))
  #yearTrend = Briefs.objects.order_by('frequency')[:10].values(ExtractYear('received')).annotate(frequency=Count('received'))
  #byOfficer = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  #byConsultant = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  #sectorsx = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  #sectorsx = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  #sectorsx = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  #sectorsx = Briefs.objects.order_by('frequency').values('sector2').annotate(frequency=Count('brief_id'))
  context = {
            "sector":bySector,
            "category":byCategory,
            #"objectx":sectorsx,
            "locations":byLocation,
            "byYear":yearTrend,
            "byDeveloper":byDeveloper
    }

  #Members.objects.values('designation').annotate(dcount=Count('designation')) #akin to SELECT designation, COUNT(designation) AS dcount FROM members GROUP BY designation
  dir(yearTrend)
  return render(request = request, template_name = 'pulse/grouped.htm', context=context)
  #return render(request = request, template_name = 'pulse/grouped.htm', context={"grouped_list":Briefs.objects.order_by('-brief_id')})
  

def project_create_view2(request):
    context = {}
    return render(request, "pulse/captureAcknowledgement.htm", context)

def BriefDetailView4(request, pk):
    return HttpResponse("You're voting on question %s." % 255655)
    #sme = pk
    #brief = get_object_or_404(Briefs, sme)
    #print(pk)
    #return render(request, 'pulse/detail.htm', {'brief_details': brief})

class BriefDetailView(View):
      def get(self, request, *args, **kwargs):  #    brief_id
          brief = get_object_or_404(Briefs, pk=brief_id)
          print(brief)
          return render(request, 'pulse/detail.htm', {"brief_details":brief})

          #try:
          #    brief = Briefs.objects.get(pk=brief_id)
          #except Briefs.DoesNotExist:
          #    raise Http404("brief does not exist")
          #return render(request, 'pulse/detail.htm', {'brief_details': brief})

          #brief = get_object_or_404(Briefs, pk=kwargs['pk'])
          #context = {'brief': brief} #kana kere brief_details??    #return render(request, 'pulse/detail.htm', context)
          #print(brief)
          #return render(request, 'pulse/detail.htm', {"brief_details":Briefs.objects.order_by('-brief_id')[:3]})   # brief

class PulseView(View):
    template_name = 'pulse/pulse.htm'
    context_object_name = 'current_brief_list'
    #def get_queryset(self):
      #return HttpResponse('Class based view')
      #return Briefs.objects.order_by('brief_id')[:15]
      #return render(request,"pulse/pulse.htm")
      
    def get(self,request):
      return render(request,'pulse/pulse.htm')
      #return Briefs.objects.order_by('brief_id')
    def post(self,request):
      return render(request,template_name)

"""
def pulse(request):
    return render(request,"pulse/pulse.htm")
"""
def pelo(request):
  return render(request = request, template_name = 'pulse/pulse.htm', context={"current_brief_list":Briefs.objects.order_by('-brief_id')})

def thaloso(request,*args,**kwargs):
  brief_details = get_object_or_404(Briefs, pk=Briefs.brief_id)
  #return HttpResponse(brief_details)
  #"details, details, things to do things to get done, dont bother me with details just tell me when they are done.")
  return render(request = request, template_name = 'pulse/detail.htm', context={"brief_details":Briefs.objects.order_by('brief_id')})

def post_new(request):
    form = PostForm()
    return render(request = request, template_name = 'pulse/brief.htm', context = {'form':form})

def new_brief(request):
    form = PostForm()
    return render(request = request, template_name = 'pulse/brief.htm', context = {'form':form})

def hello(request):
    text = '<h1>welcome to my app, doing it, doing it, and doing it well!</h1>'
    #return HttpResponse(text)
    """ or the following """
    return render(request,"pulse/hello.htm")



"""
def detail(request, question_id):
    question = get_object_or_404(Categories, pk=category_id)
    return render(request, 'pulse/detail.htm', {'category': category})


class HelloView(View):
    template_name = 'pulse/hello.htm'
    text = '<h1>welcom to my app !</h1>'
    def get(request):
        return HttpResponse(text)
"""


