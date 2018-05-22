from .models import Word
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import WordForm


def word_list(request):
    return render(request,'dostdict/word_list.html')


def starts_with(request,pk):
    words= Word.objects.filter(word_title__startswith=pk)
    return render(request, 'dostdict/word_starts_all.html', {'words': words})


def add_word(request):
    if request.method =="POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'dostdict/add_word.html',{'form':form})


def word_delete(request,pk):
    word=get_object_or_404(Word ,pk=pk)
    word.delete()
    return redirect('word_list')





# Create your views here.
