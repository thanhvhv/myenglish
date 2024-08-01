from django.shortcuts import render
from .models import ListWord, Word
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.

def home(request):
    list_words = ListWord.objects.all()
    words = list(Word.objects.all())
    for word in words:
        if word.new_word == False:
            duration = (timezone.now()-word.created).days
            deadline = word.deadlineReview - duration
            if deadline < 0:
                deadline = 0
            word.deadlineReview = deadline
            word.save()
    if request.method == "POST":
        new_word = Word()
        if request.POST.get('word') is not None:
            list_word = ListWord.objects.filter(title=request.POST.get('listWord')).first()
            print(list_word)
            new_word.listWord=list_word
            new_word.word=request.POST.get('word')
            new_word.type=request.POST.get('type')
            new_word.level=request.POST.get('level')
            new_word.pronunciation=request.POST.get('pronunciation')
            new_word.image=request.POST.get('image')
            new_word.definition=request.POST.get('definition')
            new_word.meanning=request.POST.get('meanning')
            new_word.example=request.POST.get('example')
            new_word.note=request.POST.get('note')
            new_word.save()
    context = {"list_words":list_words, "words":words}
    return render(request, "base/home.html", context)

def study(request, pk):
    words = serializers.serialize("json", Word.objects.filter(listWord__id=pk))
    context = {"words":words}
    return render(request, "base/study.html", context)

def review(request, pk):
    words_query = Word.objects.filter(listWord__id=pk)
    total_word = Word.objects.filter(listWord__id=pk).count()
    words = serializers.serialize("json", Word.objects.filter(listWord__id=pk))
    context = {"words":words, "words_query":words_query, "total_word":total_word}
    return render(request, "base/review.html", context)

def update_word(request):
    if request.method == 'POST':
        if request.POST.get("level") is not None:
            if word.new_word == True:
                word.new_word = False
            word = Word.objects.get(id=request.POST.get("idWord"))
            word.level = request.POST.get("level")
            response_data = {
                'message': 'Rating received successfully!',
            }
            return JsonResponse(response_data)
        
        return JsonResponse({'error': 'Invalid request'}, status=400)

    return render(request, "base/home.html")
