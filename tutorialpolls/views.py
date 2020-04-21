from .models import Question, Choice
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.

# Get and display questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'tutorialpolls/index.html', context)


# Show questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Deadend friendo, question does not exist")
    return render(request, 'tutorialpolls/detail.html', {'question': question})

# Display results for a specific question
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'tutorialpolls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #magic
    except (KeyError, Choice.DoesNotExist):
        # redisplay voting form instead
        return render(request, 'tutorialpolls/detail.html', 
            {
                'question': question,
                'error_message': "Please select a valid choice",
            }
        )
    else:
        # update model object attr value and save
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('tutorialpolls:results', args=(question.id,)))

        
