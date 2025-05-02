from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    number = models.CharField(max_length=10, unique=True)  # e.g., Q01
    text = models.TextField()
    is_likert = models.BooleanField(default=False)  # True for questions with Likert scale
    is_text = models.BooleanField(default=False)  # True for questions expecting a text response

    def __str__(self):
        return f"{self.number}: {self.text[:50]}..."

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses')
    created_at = models.DateTimeField(auto_now_add=True)

class ResponseOption(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='selected_options')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)  # Null for text responses
    text_response = models.TextField(null=True, blank=True)  # For text-based answers
    likert_value = models.IntegerField(null=True, blank=True)  # For Likert scale responses (1-5)

    class Meta:
        unique_together = ('response', 'question', 'option')