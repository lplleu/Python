from django.contrib import admin
from django.urls import path
#from django.conf.urls import patterns, include, url
#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url


admin.autodiscover()

from . import views

app_name = 'pulse'

urlpatterns = [
    # ex: /polls/
    #path('', include('pulse.urls')),
    path('', views.IndexView.as_view(), name='index'),
    path('pulse', views.pelo, name='pulse'),
    path('pulse/', views.pelo, name='pulse'),

    path('pulse/<int:pk>/', views.briefDetailView2, name='detail'),
                                                       
    path('<int:pk>/', views.briefDetailView2, name='detail'),
                                                 
    path('addOfficer/', views.addOfficer, name='detail'),

    path('acknowledge/', views.project_create_view, name='detail'),

    path('css/', views.cssView, name='detail'),
    path('boardView/<int:pk>/', views.boardView, name='detail'),
    path('letter/<int:pk>/', views.letterView, name='detail'),
    path('grouped/', views.grouped, name='detail'),
    path('comment/<int:pk>/', views.commentView, name='detail'),

    path('pulse/officer/<int:pk>/', views.officerDetailView, name='detail'),
    path('pulse/pb/<int:pk>/', views.pbDetailView, name='detail'),

    path('assignPB/', views.assignPB, name='detail'),

    path('confirmDelete/<int:id>', views.project_delete_view, name='detail'),

    path('editPB/<int:id>', views.project_edit_view, name='detail'),

    path('new', views.post_new, name='new_brief'),

    url(r'^hello', views.hello),

    url(r'^<int:pk>', views.hello),
]
