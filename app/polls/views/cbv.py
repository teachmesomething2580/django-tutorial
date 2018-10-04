# class based view
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic.base import View

from ..models import Question, Choice


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    ordering = ('-pub_date',)

    def get_queryset(self):
        return super().get_queryset()[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    pk_url_kwarg = 'question_id'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    pk_url_kwarg = 'question_id'

class VoteView(View):
    def post(self, request, question_id):
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