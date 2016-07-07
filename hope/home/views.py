from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import News

def index(request):
	news = News.objects.filter(active=1).order_by('-pub_date')
	return HttpResponse(news)