from django.shortcuts import render
from .models import Entry
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'myapp/post_list.html' , {'entries': entries})

def post_detail(request, pk):
    entries = get_object_or_404(Entry, pk=pk)
    return render(request, 'myapp/post_detail.html', {'entries': entries})