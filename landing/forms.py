from django import forms
from .models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('',)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('',)

class FullQuestionForm(forms.ModelForm):
    class Meta:
        model = FullQuestion
        exclude = ('',)

