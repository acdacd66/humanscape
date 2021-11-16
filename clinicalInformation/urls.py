from django.contrib import admin
from django.urls import path,include
import clinicalInformation.views as views

urlpatterns = [
        path('batch/', views.BatchDataView.as_view(),name='batch'),
        path('search/', views.ClinicalDataSearchView.as_view(),name='search'),
        path('list/', views.ClinicalDataListView.as_view(),name='list'),
       
]

