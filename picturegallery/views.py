from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *

def show_about_page(request):
    print("about page request")
    name='Sparshi Kapil'
    email='sparshi.17bcs1005@abes.ac.in'
    data={'name':name,'email':email}
    return render(request,"about.html",data)
def show_home_page(request):
    cat=Category.objects.all()
    images=Image.objects.all()
    data={'images':images,'cat':cat}
    return render(request,"home.html",data)
def show_category_page(request,cid):
    cats = Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}
    return render(request, "home.html", data)
def home(request):
    return redirect('/home')
