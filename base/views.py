from django.shortcuts import render
from .models import ListWord, Word
from django.core import serializers
# Create your views here.

def home(request):
    list_words = ListWord.objects.all()
    words = list(Word.objects.all())
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

def study(request):
    words = serializers.serialize("json", Word.objects.all())
    print(words)
    context = {"words":words}
    return render(request, "base/study.html", context)