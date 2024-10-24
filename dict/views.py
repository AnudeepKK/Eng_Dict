from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search = request.GET.get('search')
    dict = PyDictionary()
    meaning = dict.meaning(search)
    synonyms = dict.synonym(search)
    antonyms = dict.antonym(search)
    if meaning==None:
        return render(request,'index.html')
    meanings_items = list(meaning.items())
    if meaning==None:
        return render(request,'index.html')
    
    return render(request,'word.html',{'meanings':meanings_items,'synonyms':synonyms,'antonyms':antonyms})