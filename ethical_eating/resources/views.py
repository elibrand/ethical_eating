from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from resources.models import Questions
from resources.forms import QuestionForm


def index(request):
    return render(request, 'resources/index.html')


def questions(request):
    queries = Questions.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for asking, dude')
    else:
        form = QuestionForm()
    return render(request, 'resources/questions.html', {'form': form, 'queries': queries})


def resources(request):
    return render(request, 'resources/resources.html')


def books(request):
    return render(request, 'resources/books.html')


def sources(request):
    return render(request, 'resources/sources.html')


def products(request):
    return render(request, 'resources/products.html')


def about(request):
    return render(request, 'resources/about.html')