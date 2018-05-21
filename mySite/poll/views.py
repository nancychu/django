from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question
from django.template import loader
from django.urls import reverse


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('poll/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context,request))

def detail(request, question_id):
		question = get_object_or_404(Question,pk=question_id)
		return render(request,'poll/detail.html',{'question':question}) #render()函数 https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial03/

def results(request, question_id):
	response = "you're looking at the results of question %s ////"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you're voting on question %s." % question_id)