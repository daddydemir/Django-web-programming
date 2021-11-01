from django.shortcuts import render
from .models import Entry
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'myapp/post_list.html' , {'entries': entries})

def post_detail(request, pk):
    entries = get_object_or_404(Entry, pk=pk)
    return render(request, 'myapp/post_detail.html', {'entries': entries})

def post_new(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail' , pk=post.pk)
    else:
        form = PostForm()
    return render(request , 'myapp/post_edit.html' , {'form':form})
