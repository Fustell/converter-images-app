from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request, 'converter_images/index.html', {'title':'Конвертер зображень'})

def upload_image(request):
    return HttpResponse("Success uploaded")