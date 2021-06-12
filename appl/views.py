from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import *

def home(request):
    products=product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


def pro(request):
	products=product.objects.all()
	context = {'products':products}
	return render(request, 'pro.html', context)

def contact(request):
    if request.method== 'POST':
      name =request.POST['name']
      email =request.POST['email']
      message =request.POST['message']
      send_mail(
           name,
           message + '\n email : ' + email,
           email,
           ['mithileshkrishna2000@gmail.com'],
           fail_silently=False)
    return render(request, 'contact.html')

def customer(request) :
    if request.method== 'POST':
        name=request.POST['name']
        pno=request.POST['pno']
        product=request.POST['prod']
        print("check",name,pno)
        ins=Customer(name=name,pno=pno,product=product)
        ins.save()
        send_mail(
           name,
           '\n phone no : '+ pno + '\n product : ' + product,
           'deveewebsite@gmail.com',  
           ['mithileshkrishna2000@gmail.com'],
           fail_silently=False)
    return redirect('pro')
    #return render(request, 'pro.html')


def search(request): 
    q =request.GET['q']
    data= product.objects.filter(product_name__icontains=q).order_by('product_name') 
    return render(request, 'search.html', {"data":data})

def view(request,id) :
    products = get_object_or_404(product,pk=id)
    return render(request, 'view.html',{'products':products})

def check(request,id) :
    productss = get_object_or_404(product,pk=id)
    return render(request, 'check.html',{'productss':productss})