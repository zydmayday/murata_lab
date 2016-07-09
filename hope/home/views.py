from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import News


def index(request):
	news = News.objects.filter(active=1).order_by('-pub_date')
	template = loader.get_template('index.html')
	context = {
		'news': news
	}
	return HttpResponse(template.render(context, request))

