from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'entries/journal.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form' : form}
    return render(request, 'entries/add.html', context)

def editEntry(request, pk):
    entry = Entry.objects.get(id=pk)

    form = EntryForm(instance=entry)

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 'entries/update.html', context)

def deleteEntry(request, pk):
    entry = Entry.objects.get(id=pk)

    if request.method == 'POST':
        entry.delete()
        return redirect('/')

    context = {'entry' : entry}
    return render(request, 'entries/delete.html', context)

def search(request):
    query = request.GET.get('q','')
    if query:
        queryset = (Q(title__icontains=query) | Q(text__icontains=query))
        results = Entry.objects.filter(queryset).distinct()
    else:
       results = []
    
    return render(request, 'entries/search.html', {'results':results, 'query':query})
