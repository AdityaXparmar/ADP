from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.db.models import Q

def note_list(request):
    query = request.GET.get('q')

    if query:
        notes = Note.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        notes = Note.objects.all().order_by('-created_at')

    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'query': query
    })


def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(title=title, content=content)
        return redirect('note_list')

    return render(request, 'notes/note_form.html')


def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')

    return render(request, 'notes/note_form.html', {'note': note})


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')




