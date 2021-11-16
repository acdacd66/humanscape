import re
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .models import ClinicalData
import datetime
from django.http import Http404
from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from .serializers import ClinicalDataSerializer

from django.db.models import DurationField, F, ExpressionWrapper
from rest_framework.pagination import LimitOffsetPagination
from django.conf import settings

def get_clinical_data():
    api_key = settings.API_KEY
    url = "https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?page=1&perPage=0&serviceKey=" + str(api_key)
    api_request = requests.get(url)
    try:
      api_request.raise_for_status()
      return api_request.json()
    except:
      return None

def compare_old_and_new(old,new,obj,updated_flag):
    if updated_flag == True:
        if old == new:
            return new
        else:
            obj.updated_at = datetime.datetime.today()
            return new
    else:
        return new

def save_clinical_data(clinical_data):
    update_flag = False
    datas = clinical_data['data']
    for d in datas:
        clinicalData = None
        if ClinicalData.objects.filter(taskCode = d["과제번호"]).exists():
            clinicalData = ClinicalData.objects.get(taskCode = d["과제번호"])
            update_flag = True
       
        else:
            clinicalData = ClinicalData()
        
        
        clinicalData.taskCode = compare_old_and_new(clinicalData.taskCode ,d["과제번호"],update_flag,clinicalData)
        
        clinicalData.taskName = compare_old_and_new(clinicalData.taskName, d["과제명"],update_flag,clinicalData)
        clinicalData.department = compare_old_and_new( clinicalData.department,d["진료과"],update_flag,clinicalData)
        clinicalData.chiefInstitution = compare_old_and_new( clinicalData.chiefInstitution,d["연구책임기관"],update_flag,clinicalData)
        if d["전체목표연구대상자수"] != "":
             clinicalData.studySubjectNumbers = compare_old_and_new(clinicalData.studySubjectNumbers, int(d["전체목표연구대상자수"]), update_flag,clinicalData)

        
        if d["연구기간"][-2:] == "개월":
            clinicalData.studyPeriod = compare_old_and_new(clinicalData.studyPeriod,int(d["연구기간"][:-2]),update_flag,clinicalData)
        try:
            if d["연구기간"][-1:] == "년":
                clinicalData.studyPeriod = compare_old_and_new(clinicalData.studyPeriod,int(d["연구기간"][:-1]) * 12,update_flag,clinicalData)
        except:
            pass
        clinicalData.studyType = compare_old_and_new(clinicalData.studyType, d["연구종류"],update_flag,clinicalData)
        clinicalData.studyPhase = compare_old_and_new(clinicalData.studyPhase , d["임상시험단계(연구모형)"],update_flag,clinicalData)
        clinicalData.studyScope = compare_old_and_new( clinicalData.studyScope, d["연구범위"],update_flag,clinicalData)

        # if len(clinicalData.tracker.changed()) >  0:
        #     clinicalData.updated_at = datetime.datetime.today()

        clinicalData.save()
       
        
        


class BatchDataView(APIView):
    def post(self, request = None):
        clinical_data = get_clinical_data()
       
        if clinical_data is not None:
            save_clinical_data(clinical_data)
        
            
        return Response(status=status.HTTP_200_OK)


class ClinicalDataSearchView(APIView):
    def get(self, request):

        input_key = None
        if request.query_params.get("taskCode", None) is not None:
            input_key = request.query_params.get("taskCode")

        response = None

        try:
            clincal_object = ClinicalData.objects.get(taskCode = input_key)
            response = ClinicalDataSerializer(clincal_object)
        except:
            raise Http404

        return JsonResponse({'Message':response.data}, status=200)

class ClinicalDataListView(APIView,LimitOffsetPagination):
    
    def get(self, request):
        today = datetime.datetime.today()
        last_delta = datetime.timedelta(7)
        last_week_date = today- last_delta
    
        updated_datas = ClinicalData.objects.filter(updated_at__range = [last_week_date, today])
        
        page = self.paginate_queryset(updated_datas,request, view=self)
        
        serializer = ClinicalDataSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

            