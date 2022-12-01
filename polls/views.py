from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
# Create your views here.
# class Poll:
#     def __init__(self, question_text, pub_date):
#         self.question_text = question_text
#         self.pub_date = pub_date
        
#     def __str__(self):
#         return f"{self.question_text}"

# polls = [
#     Poll('Question1', '12/1/22'),
#     Poll('Question2', '11/28/22'),
# ]

# def index(request):
#     return render(request, 'index.html',{'polls':polls})