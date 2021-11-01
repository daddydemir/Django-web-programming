from django.shortcuts import render
from .models import Entry
from django.utils import timezone

# Create your views here.

def post_list(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'myapp/post_list.html' , {'entries': entries})