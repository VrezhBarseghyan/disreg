from django.shortcuts import render
from .forms import *


# Create your views here.
def index(request):
    form = EmailForm()
    form2 = QuestionForm()

    if request.method == "POST":
        form = EmailForm(request.POST)
        form2 = QuestionForm(request.POST)

        if form.is_valid() & form2.is_valid():
            email = form.save()
            question = form2.save()

            full_question = FullQuestion(email=email, question=question)
            form1 = FullQuestionForm(request.POST, request.FILES, instance=full_question)

            if form1.is_valid():
                form1.save()

    return render(request, 'homePage/home.html', {'form': form,
                                                  'form2': form2})
