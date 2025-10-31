import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Compliment, SharedCompliment

def home(request):
    return render(request, 'compliments/home.html')

def get_random_compliment(request):
    compliments = Compliment.objects.all()
    if compliments:
        compliment = random.choice(compliments)
        return JsonResponse({'text': compliment.text, 'id': str(compliment.id)})
    return JsonResponse({'text': 'You are amazing! ✨'})

def share_compliment(request, compliment_id):
    compliment = get_object_or_404(Compliment, id=compliment_id)
    shared = SharedCompliment.objects.create(compliment=compliment)
    compliment.share_count += 1
    compliment.save()
    share_url = f"{request.build_absolute_uri('/shared/')}{shared.id}/"
    return JsonResponse({'share_url': f'/shared/{shared.id}', 'success': True})

def view_shared(request, share_id):
    shared = get_object_or_404(SharedCompliment, id=share_id)
    return render(request, 'compliments/shared.html', {'compliment': shared.compliment})
