from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
'''
def home(request):
    received_text = None

    if request.method == "POST":
        received_text = request.POST.get('text_input')  # Formdan gelen veriyi al

    return render(request, 'home.html', {'received_text': received_text})
'''
from django.shortcuts import render
from django.http import JsonResponse
'''
@csrf_exempt
def home(request):
    received_text = None
    if request.method == "POST":
        received_text = request.POST.get('text_input')  # Formdan gelen veriyi al

    return render(request, 'home.html', {'received_text': received_text})
@csrf_exempt
def get_text(request):
    # ESP8266 bu yola GET isteği yaparak veriyi alacak
    received_text = request.GET.get('text', '')
    return JsonResponse({'text': received_text})
'''
from .models import TextData
@csrf_exempt
def home(request):
    received_text = None
    if request.method == "POST":
        received_text = request.POST.get('text_input')  # Formdan gelen veriyi al
        TextData.objects.create(text_input=received_text)  # Veritabanına kaydet

    return render(request, 'home.html', {'received_text': received_text})

# ESP8266'nın veriyi çekeceği fonksiyon
@csrf_exempt
def get_text(request):
    # En son kaydedilen text verisini al
    latest_text = TextData.objects.last()
    if latest_text:
        return JsonResponse({'text': latest_text.text_input})
    else:
        return JsonResponse({'text': 'Veri yok'})  # Eğer veri yoksa 'Veri yok' döner