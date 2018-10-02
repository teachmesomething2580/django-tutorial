from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    # 곧바로 /polls로 redirect 되도록 설정
    return redirect('index')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
