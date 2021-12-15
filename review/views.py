from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Review


def home(request):
    return render(request, 'review/review.html')

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'body', 'image']

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['title', 'body', 'image']

class ReviewDeleteView(DeleteView):
    model = Review
    fields = ['title', 'body', 'image']
