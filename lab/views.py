from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import MyModel
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response


# from django.db import models
def Home(request):
    MyModel.objects.create(username="masum", city="comilla")
    return HttpResponse("success")


def failed(request):
    return JsonResponse({"id": "1", "name": "cmasum"})


@api_view(["GET", "POST"])
def view(request):
    data = MyModel.objects.all()
    serializers = userDataSerial(data=request.data)
    if (request.method == "GET"):
        serializers = userDataSerial(data, many=True)
        return Response(serializers.data)
    elif (request.method == "POST"):
        serializers = userDataSerial(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return HttpResponse("success")
    return Response(serializers.errors)


@api_view(["GET","POST"])
def deleteItem(request):
    data = MyModel.objects.all().filter(username=request.data['username'])
    if request.method == "POST":
        if data:
            data.delete()
            return HttpResponse("successfully delete")
        else:
            return HttpResponse("No Data")
    return HttpResponse("Try With Post Method")
    # return HttpResponse("no data have")


@api_view(["GET","POST"])
def ChildData(request):
     # serializers = userChildSerial(data=request.data)
     # data =  ChildTable.objects.create(mobile_id=request.data['mobile'],married=request.data['married'])
     # print(data)
     data = ChildTable.objects.all()
     serialize = userChildSerial(data,many=True)
     return  Response(serialize.data)