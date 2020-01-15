from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.http import HttpResponseRedirect
from resources.models import Questions, Book, Restaurant, Review, Product
from resources.forms import QuestionForm, ReviewForm, QuizForm
from resources.repositories import bible_sources


def index(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            congrats = ''
            score = sum([q.points for q in form.cleaned_data.values()])
            print(score)
            if 60 <= score < 79:
                messages.info(request,
                              message='Congratulations, you are a chosen meat-lover. Feel free to read more about us')
                return redirect(reverse('resources:about'))
            elif 50 <= score < 60:
                messages.info(request,
                              message='Congratulations, you are a mindful meat-eater. Check out our forum for more '
                                      'insight')
                return redirect(reverse('forum:forum'))
            elif 40 <= score < 50:
                messages.info(request,
                              message='Congratulations, you are an ethical omnivore. Check out our forum for more '
                                      'insight')
                return redirect(reverse('forum:forum'))
            elif 35 <= score < 40:
                messages.info(request,
                              message='Congratulations, you are an enlightened pescatarian. Check out our FAQs for '
                                      'more insight')
                return redirect(reverse('resources:questions'))
            elif 30 <= score < 35:
                messages.info(request,
                              message='Congratulations, you are a jewy vegetarian. Check out all the products and '
                                      'restaurants available ')
                return redirect(reverse('resources:about'))
            elif 19 <= score < 30:
                messages.info(request,
                              message='Congratulations, you are a holy vegan. Feel free to register if you should like')
                return redirect(reverse('users:register'))
            print(congrats)
            # 60 - 78 > chosen meat-lover -> .container:hover .gauge-c {  transform:rotate(.08turn);
            # 50 - 60 > mindful meat-eater -> .container:hover .gauge-c {  transform:rotate(.17turn);
            # 40 - 50 > ethical omnivore -> .container:hover .gauge-c {  transform:rotate(.25turn);
            # 35 - 40 > enlightened pescatarian -> .container:hover .gauge-c {  transform:rotate(.33turn);
            # 30 - 35 > jewy vegetarian -> .container:hover .gauge-c {  transform:rotate(.42turn);
            # 19 - 30 > holy vegan -> .container:hover .gauge-c {  transform:rotate(.5turn);

    else:
        form = QuizForm()
    return render(request, 'resources/index.html', {'form': form})


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
    books = Book.objects.all().order_by('-id')[:4]
    restaurants = Restaurant.objects.all().order_by('-id')[:1]
    products = Product.objects.all().order_by('-id')[:4]
    return render(request, 'resources/resources.html', {'books': books, 'restaurants': restaurants, 'products': products})


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
    products = Product.objects.all()
    return render(request, 'resources/products.html', {'products': products})


def bible(request):
    return render(request, 'resources/bible.html', {'bible': bible_sources})


def talmud(request):
    return render(request, 'resources/talmud.html')


def rabbis(request):
    return render(request, 'resources/rabbis.html')


def thinkers(request):
    return render(request, 'resources/thinkers.html')


def about(request):
    return render(request, 'resources/about.html')


def why(request):
    return render(request, 'resources/why.html')

