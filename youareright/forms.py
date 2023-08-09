from django import forms
from .models import Board, Reply, Hashtag

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['category', 'title', 'content', 'author'] 

class Reply(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply', 'comment', 'rep_date'] 