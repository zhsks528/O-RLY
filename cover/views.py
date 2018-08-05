from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoverForm
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from .utils import COLOR_CODES

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST, request.FILES)
        if form.is_valid():
            pass   #이미지를 생성할 데이터는 여기에 있고!!
    else:
        form = CoverForm()
    return render(request, 'cover/index.html',{
        'form':form,
    })

def image_generator(request):
    title = request.GET['title']
    top_text = request.GET['top_text']
    author = request.GET['author']
    animal_code = request.GET['animal_code']
    color_index = request.GET['color_code']
    guide_text = request.GET['guide_text']
    guide_text_piacement = request.GET['guide_text_piacement'] 

    animal_path = settings.ROOT('assets', 'animal', '{}.png'.format(animal_code))
    animal_im = Image.open(animal_path)
    animal_im = animal_im.resize((400,400))

    color = COLOR_CODES[int(color_index)]

    canvas_im = Image.new('RGB',(500, 700), 'white')
    canvas_im.paste(animal_im, (50,40)) #left/top 지정

    ttf_path = settings.ROOT('assets','fonts','NanumGothic.ttf')
    draw = ImageDraw.Draw(canvas_im)

    draw.rectangle((20, 0, 480, 10), fill = color)

    draw.rectangle((10, 400, 400, 510), fill = color)

    fnt = ImageFont.truetype(ttf_path, 70)
    draw.text((45, 430), title, font=fnt, fill=(255, 255, 255, 255))

    fnt = ImageFont.truetype(ttf_path, 20)
    draw.text((160, 15), top_text, font=fnt, fill=(0, 0, 0, 255))
    
    fnt = ImageFont.truetype(ttf_path, 25)
    draw.text((360, 655), author, font=fnt, fill=(0, 0, 0, 255))

    fnt = ImageFont.truetype(ttf_path, 30)
    draw.text((120, 500), guide_text, font=fnt, fill=(0, 0, 0, 255))

    response = HttpResponse(content_type='image/png')
    canvas_im.save(response, format='PNG')
    return response

