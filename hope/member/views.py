from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Member

def index(request):
	members = Member.objects.all()
	template = loader.get_template('member/index.html')
	context = {
		'members': members
	}
	return HttpResponse(template.render(context, request))

def member(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'member/member.html', {'member': member})
