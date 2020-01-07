from django.contrib import messages
from django.urls import reverse

from forum.forms import ThreadForm
from forum.models import Thread

from django.shortcuts import render, redirect


# Create your views here.


def forum(request):
    threads = Thread.objects.all()
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
    return render(request, 'forum/forum.html', {'threads': threads, 'form': form})


def forum_all(request):
    threads = Thread.objects.all()
    return render(request, 'forum/forum_all.html', {'threads': threads})
