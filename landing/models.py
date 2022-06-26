from django.db import models
from django.core.validators import RegexValidator

# Create your models here.]

# EMAIL_VALIDATOR = RegexValidator(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', 'only valid email is required')


class User(models.Model):
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.email

class Question(models.Model):
    question = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.question

class FullQuestion(models.Model):
    email = models.CharField(max_length=200, null=True)
    question = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.email + " asked: " + self.question
