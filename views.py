from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import myCurdForm
from .models import mycurd


# Create your views here.

def mycurd_list(request):
   # return(HttpResponse("Hello World!"))
   mycurds = mycurd.objects.all()
   context={
      "mycurd_list": mycurds
   }
   print(mycurds)
   return render(request,"mycurd/mycurd_list.html", context)

def mycurdDetails(request, id):
   mycurds = mycurd.objects.get(id=id)
   context = {
      "mycurd": mycurds  #mycurds
   }
   return render(request,"mycurd/mycurdDetails.html", context)

def mycurdCreate(request):
   
   form=myCurdForm(request.POST or None)
   if form.is_valid():
      name=form.cleaned_data['name']
      due_date=form.cleaned_data['due_date']
      print(name, due_date)
      form.save()
      return redirect('/')
   context = {"form": form
   } 
   return render(request, "mycurd/CurdForm.html", context)
   
def curdUpdate(request, id):
   mycurdupdate = mycurd.objects.get(id=id)
   form=myCurdForm(request.POST or None, instance=mycurdupdate)
   if form.is_valid():
      form.save()
      return redirect('/')
   context = {"form": form
   }
   return render(request,"mycurd/mycurdUpdate.html", context)


def curdDelete(request, id):
   curdDelete = mycurd.objects.get(id=id)
   curdDelete.delete()
   return redirect("/")

   
