from django.db import models

# Create your models here.
class ListWord(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    totalWord = models.IntegerField(default=0)
    totalStudy = models.IntegerField(default=20) 
    wordReview = models.IntegerField(default=0)
    easyWord = models.IntegerField(default=0)
    mediumWord = models.IntegerField(default=0)
    hardWord = models.IntegerField(default=0)  
    ratioEasyWord = models.IntegerField(default=0)
    ratioMediumWord = models.IntegerField(default=0)
    ratioHardWord = models.IntegerField(default=0)  
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Word(models.Model):
    listWord = models.ForeignKey(ListWord, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    WORD_CHOICES = (
        ("noun", "noun"),
        ("verb", "verb"),
        ("adj", "adj"),
        ("adv", "adv"),
        ("pronoun", "pronoun"),
        ("preposition", "preposition"),
        ("conjunction", "conjunction"),
        ("interjection", "interjection"),
    )
    type = models.CharField(max_length=15, choices=WORD_CHOICES, default=None)
    LEVEL_CHOICES = (
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    )
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=None)
    pronunciation = models.CharField(max_length=50)
    image = models.CharField(max_length=200, blank=True)
    definition = models.TextField(blank=True)
    meanning = models.CharField(max_length=50)
    example = models.TextField(blank=True)
    note = models.TextField(blank=True)

    DIFFICULTY_CHOICES = (
        ("Easy","Easy"),
        ("Medium","Medium"),
        ("Hard","Hard")
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="Hard")
    memoryLevel = models.IntegerField(default=1)  
    deadlineReview = models.IntegerField(default=1)  
    new_word = models.BooleanField(default=True)
    totalReview = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.word