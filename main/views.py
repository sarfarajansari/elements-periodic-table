from django.shortcuts import render
from .forms import atomicnameform
import json
from .object import dataobject

# Create your views here.

with open('data.json') as f:
    data = json.load(f)


def index(request):
    return render(request, 'main/index.html',{
        "nameform":atomicnameform
    } )

def error(request):
    return render(request,"main/error.html")

def search(request):
    try:
        value = request.GET["q"]
    except:
        return error(request)
    for element in data:
        if str(value).lower()== str(element["name"]).lower() or str(value).lower()== str(element["atomicNumber"]).lower() or str(value).lower()== str(element["symbol"]).lower() :
            requested_element =dict(element)
            datalist=[]
            for ele in requested_element:
                datalist.append(dataobject(ele,requested_element[ele]))
            return render(request,"main/table.html",{
                "data": datalist
            })
    return error(request)