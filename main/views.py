from django.shortcuts import render
import requests
from django.http import JsonResponse


API_URL = "https://nacos.pythonanywhere.com/api/v1/"

def index(request):
    endpoint = "courses-available"
    url = API_URL + endpoint
    r = requests.get(url)
    response = r.json()
    courses = response['courses']
    return render(request, 'main/index.html', context={'courses': courses})

def course_questions(request, course):
    endpoint = f"{course}/questions"
    url = API_URL + endpoint
    r = requests.get(url)
    response = r.json()
    num_questions = len(response)
    context = {
        "response": response, "course": course, "num": num_questions
    
    }
    return render(request, 'main/questions_page.html', context)
