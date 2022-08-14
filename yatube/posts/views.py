from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('О БОГИ!!!, это было блестяще....')


def group_posts(request, slug):
    return HttpResponse(f'Вот что хочешь ты здесь увидеть? Может это? {slug}...Ты сам этого захотел')

# Create your views here.
