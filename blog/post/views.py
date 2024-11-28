from django.shortcuts import render, HttpResponse

def post_view(request):
    return HttpResponse('Hola bo.')
