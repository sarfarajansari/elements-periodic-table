from django.shortcuts import render
from .forms import atomicnumberform,atomicsymbolform,atomicnameform,nameclicked,numberclicked,symbolclicked
import json
from .object import dataobject

# Create your views here.

with open('data.json') as f:
    data = json.load(f)

def index(request):
    clickednumber=0
    if request.method == "GET":
        form= atomicnumberform
        return render(request, 'main/index.html',{
            "numberform": form,"symbolform": atomicsymbolform,"nameform":atomicnameform, "numberclicked":numberclicked,"symbolclicked":symbolclicked,"nameclicked":nameclicked,"clickednumber":clickednumber
        } )
    else:
        
        form = atomicnameform(request.POST)
        if form.is_valid():
            key = form.cleaned_data["key"]
            print(key)
            value=form.cleaned_data["value"]
            print(value)
            for element in data:
                if str(value).lower()== str(element[key]).lower():
                    
                    requested_element =dict(element)
                    datalist=[]
                    for ele in requested_element:
                        datalist.append(dataobject(ele,requested_element[ele]))
                    return render(request,"main/table.html",{
                        "data": datalist, "numberclicked":numberclicked,"symbolclicked":symbolclicked,"nameclicked":nameclicked,"clickednumber":clickednumber
                    })
            return render(request,"main/error.html")
        else:
            return render(request,"main/error.html")


def hid(request):
    form= numberclicked(request.POST)
    if form.is_valid():
        clickednumber = form.cleaned_data["clickednumber"]
        

        return render(request, 'main/index.html',{
            "numberform": atomicnumberform,"symbolform": atomicsymbolform,"nameform":atomicnameform, "numberclicked":numberclicked,"symbolclicked":symbolclicked,"nameclicked":nameclicked,
            "clickednumber":clickednumber
        } )

def error(request):
    return render(request,"main/error.html")