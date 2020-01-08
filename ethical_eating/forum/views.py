from django.contrib import messages
from django.urls import reverse

from forum.forms import ThreadForm, CommentForm
from forum.models import Thread, Comment

from django.shortcuts import render, redirect


# Create your views here.


def forum(request):
    last_five = Thread.objects.all().order_by('-id')[:5]
    if request.method == 'POST':

        form = ThreadForm(request.POST)
        if form.is_valid():
            creator = form.cleaned_data['name']
            text = form.cleaned_data['subject']
            Thread(text=text, creator=creator).save()
            messages.success(request, 'Thanks for getting involved, dude')
            return redirect(reverse('forum:forum'))
    else:
        form = ThreadForm()
        cform = CommentForm()
    return render(request, 'forum/forum.html', {'last_five': last_five, 'form': form, 'cform': cform})


def forum_all(request):
    threads = Thread.objects.all()
    cform = CommentForm()
    return render(request, 'forum/forum_all.html', {'threads': threads, 'cform': cform})


def get_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            creator = form.cleaned_data['name']
            text = form.cleaned_data['comment']
            thread = Thread.objects.get(pk=pk)
            Comment(text=text, thread=thread, creator=creator).save()
            messages.success(request, 'Thanks for commenting, dude')
    return redirect(reverse('forum:all'))



