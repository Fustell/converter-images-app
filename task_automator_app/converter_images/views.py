from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect,Http404
from PIL import Image
from .forms import DocumentForm
from .models import Document
from django.conf import settings
import os

CONVERTED_IMAGES_ROOT = 'F:/task-automator-app/task_automator_app/media/converted_images'
DOCUMENTS_ROOT = 'F:/task-automator-app/task_automator_app/media/documents'


def index(request):
    return render(request, 'converter_images/index.html', {'title':'Головна сторінка'})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/converter_images/show_all_files/')
    else:
        form = DocumentForm()
    return render(request, 'converter_images/upload.html', {
        'form': form,
        'title': 'Конвертер зображень'
    })


def show_all_files(request):
    files = Document.objects.all()
    return render(request, 'converter_images/show_files.html', {
        'title': 'Список файлів',
        'files': files
    })


def delete_img(request,file_name):
    img = find_img_by_name(file_name)
    if img:
        img.delete()
        os.remove(os.path.join(DOCUMENTS_ROOT, file_name))
        try:
            os.remove(os.path.join(CONVERTED_IMAGES_ROOT, file_name).replace('.jpg', '.png'))
        except FileNotFoundError:
            pass
        return HttpResponseRedirect('/converter_images/show_all_files/')
    else:
        raise Http404


def convert_to_png(request,file_name):
    file = find_img_by_name(file_name)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.document))
    if os.path.exists(file_path):
        img = Image.open(file_path)
        img.save(os.path.join(CONVERTED_IMAGES_ROOT,os.path.basename(file_path)).replace('.jpg', '.png'))
        return HttpResponseRedirect(settings.MEDIA_URL+'converted_images/'+str(os.path.basename(file_path).replace('.jpg', '.png')))
    raise Http404


def find_img_by_name(file_name):
    files = Document.objects.all()
    for f in files:
        if os.path.basename(f.document.name) == file_name:
            return f
    return None