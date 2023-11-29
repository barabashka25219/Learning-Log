from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'image']
        labels = {'text': 'Topic Name', 'image': 'Also you may upload an image'}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ("text",)
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={'cols': 80})}
