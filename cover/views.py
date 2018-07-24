from django.shortcuts import render
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image
# Create your views here.

def index(request):
    if request.method == 'post':
        form = CoverForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data   #이미지를 생성할 데이터는 여기에 있고!!
            return redirect('cover:index')
    else:
        form = CoverForm()
    return render(request, 'cover/index.html',{
        'form':form,
    })

def image_generator(request):
     im = Image.new('RGB',(256,256), 'yellow')
     # im : 위 데이터를 받아서, 이미지는 여기에서 그리겠습니다.
     response = HttpResponse(content_type='image/jpeg')
     im.save(response, format='JPEG')
     return response

