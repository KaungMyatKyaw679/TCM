from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from accounts.froms import *
def dashboard(request):
    feeds=Feed.objects.all()
    return render(request,'accounts/dashboard.html',{
        'feeds': feeds
    })

def customers(request):
    return render(request,'accounts/customers.html')
def products(request):
    return render(request,'accounts/products.html')

def library(request):
    writers=Writer.objects.all()
    books=Book.objects.all()
    totalbook=books.count()
    totalwriter=writers.count()
    return render(request,'accounts/library.html',{
        'writers':writers,
        'totalbook':totalbook,
        'totalwriter': totalwriter
    })

def Bwriter(request,writerId):
    writer=Writer.objects.get(id=writerId)
    books=writer.book_set.all()

    return render(request, 'accounts/writer.html',{
        'writer':writer,
        'books':books
    })
# Create your views here.
