from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data   #이미지를 생성할 데이터는 여기에 있고!!
    else:
        form = CoverForm()
    return render(request, 'cover/index.html',{
        'form':form,
    })

def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request['animal_code']
    color_code = request['color_code']
    guide_text = request['guide_text']
    guide_text_piacement = request['guide_text_piacement'] 


    im = Image.new('RGB',(256,256), 'white')
    # im : 위 데이터를 받아서, 이미지는 여기에서 그리겠습니다.
    ttf_path = settings.ROOT('assets','fonts','NanumGothic.ttf')
    d = ImageDraw.Draw(im)

    fnt = ImageFont.truetype(ttf_path, 40)
    d.text((10, 10), title, font=fnt, fill=(0,255,0,128))
    
    fnt = ImageFont.truetype(ttf_path, 20)
    d.text((10, 60), top_text , font=fnt, fill=(0,255,0,255))
    
    fnt = ImageFont.truetype(ttf_path, 10)
    d.text((10, 100), author , font=fnt, fill=(0,255,0,255))

    response = HttpResponse(content_type='image/png')
    im.save(response, format='PNG')
    return response

