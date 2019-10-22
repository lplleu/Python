from django import forms
from .models import Briefs, Assignment, Officers
from datetime import datetime

class PostForm(forms.ModelForm):
      class Meta:
            model = Briefs
            fields = ('reference','title','locationx','recommend','sector','developer','received','exempted','tor','approved','sector2','category','notes',)

class briefForm(forms.ModelForm):
     class Meta:
           model = Briefs
           fields = [
                'brief_id',
                'sector', 
                'sector2',
                'category',
                'reference',
                'title',
                'locationx',
                'developer',
                'received'
           ]

class rawBriefForm(forms.Form):
 #    class Meta:
      #brief_id  = forms.()
      title     = forms.CharField(label='Project Title',widget=forms.TextInput(attrs={"placeholder":"e.g. Agrotourism"}))
      locationx = forms.CharField(label='Location',widget=forms.TextInput(attrs={"placeholder":"e.g. Maun"}))
      developer = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"e.g. Mokati Melelo"}))
      received  = forms.DateField() #default=Today(), widget=forms.DatePIcker()    initial=Now()

class assignForm(forms.ModelForm):
     class Meta:
           model = Assignment
           fields = [
                'project',
                'officer',
                'stage',
                'date'
           
           ]
           widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
            }
class officerForm(forms.ModelForm):
     class Meta:
           model = Officers
           fields = [
                'officer_id',
                'sname',
                'name'
           ]
