from django.shortcuts import render
from .models import Entry
from .models import Userx
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import AddUserForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request , 'myapp/post_list.html' , {'entries': entries})

def post_detail(request, pk):
    entries = get_object_or_404(Entry, pk=pk)
    return render(request, 'myapp/post_detail.html', {'entries': entries})

def user_detail(request , pk):
    userx = get_object_or_404(Userx, pk=pk)
    return render(request, 'myapp/user_detail.html', {'userx': userx})

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


def get_user(request):
    users = Userx.objects.all()
    return render(request , 'myapp/users.html' , {'users':users})

def add_user(request):
    if(request.method == 'POST'):
        form = AddUserForm(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.save()
            return redirect('user_detail' , pk=post.pk)
    else:
        form = AddUserForm()
    return render(request, 'myapp/add_user.html' , {'form': form})
