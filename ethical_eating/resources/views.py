from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from resources.models import Questions, Book, Restaurant, Review
from resources.forms import QuestionForm, ReviewForm


def index(request):
    return render(request, 'resources/index.html')


def questions(request):
    queries = Questions.objects.exclude(answer='not yet answered')
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for asking, dude. We will attempt to answer your question and post it '
                                      'as soon as possible.')
            question = form.cleaned_data['ask']
            Questions(question=question, answer='not yet answered').save()
    else:
        form = QuestionForm()
    return render(request, 'resources/questions.html', {'form': form, 'queries': queries})


# def helpful(request):


def resources(request):
    books = Book.objects.all().order_by('-id')[:3]
    restaurants = Restaurant.objects.all().order_by('-id')[:1]
    return render(request, 'resources/resources.html', {'books': books, 'restaurants': restaurants})


def books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'resources/books.html', {'books': books})


def food(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'resources/food.html', {'restaurants': restaurants})


def reviews(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for the review, buddy')
            name = form.cleaned_data['name']
            rating = form.cleaned_data['rating']
            review = form.cleaned_data['review']
            Review(rate=rating, author=name, text=review, restaurant=restaurant).save()
    else:
        form = ReviewForm()
    return render(request, 'resources/reviews.html', {'restaurant': restaurant, 'form': form})


def products(request):
    return render(request, 'resources/products.html')


def bible(request):
    return render(request, 'resources/bible.html')


def talmud(request):
    return render(request, 'resources/talmud.html')


def rabbis(request):
    return render(request, 'resources/rabbis.html')


def thinkers(request):
    return render(request, 'resources/thinkers.html')


def about(request):
    return render(request, 'resources/about.html')


def perv(request):
    return render(request, 'resources/perv.html')
