from django import forms
from .models import Entry
from .models import Userx

class PostForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title' , 'text')

class AddUserForm(forms.ModelForm):

    class Meta:
        model = Userx
        fields = ('name' , 'surname' , 'email')
        