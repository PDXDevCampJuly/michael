from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.http import HttpResponse, Http404
from polls.models import Question

# Create your views here.

# output all of the questions in a list
def questions(request):

  # grabs all of the questions from the Model Question
  question_list = Question.objects.all()

  # get the template that we want, which is questions.html
  template = loader.get_template('questions.html')

  # creates a context to return with a template in HTTPResponse
  context = RequestContext(request, {
    # it must be a dictionary!
    'question_list': question_list,
  })

  # returns the HTTPResponse with a template, that has the context
  return HttpResponse(template.render(context))


# displays the specific text and choices for each question
def details(request, question_id):

  # replaces try/except
  question = get_object_or_404(Question, pk=question_id)

  # try:
  #   question = Question.objects.get(pk=question_id)

  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")

  return render(request, 'detail.html', {'question': question})




