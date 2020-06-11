from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	mytitle="Home"
	return render(request,"page.html",{"title":mytitle})
	

def about_page(request):
	mytitle="About Us"
	return render(request,"page.html",{"title":mytitle})


def contact_page(request):
	mytitle="Contact Us"
	return render(request,"page.html",{"title":mytitle})