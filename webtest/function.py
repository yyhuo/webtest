from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    usr_text = request.GET['text']
    total_count = len(request.GET['text'])
    word_dict = {}
    for word in usr_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return render(
        request, 'count.html', {
            'count': total_count,
            'text': usr_text,
            'dict': word_dict,
            'sorted_dict': sorted_dict
        })

