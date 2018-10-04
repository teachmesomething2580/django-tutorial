from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404

from ..models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # KeyError: request.POST['choice']의 값이 없을 때
    # Choice.DoesNotExist: question.choice_set.get() 해당 값을 가져오지 못할 때
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'question': question,
                          'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id)
