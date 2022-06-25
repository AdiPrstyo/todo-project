from django.shortcuts import redirect,render
from django.http import Http404
from django.contrib import messages
# import class Task dari file todo/models.py
from .models import Task
from .forms import TaskForm

# Membuat View untuk halaman daftar task
def index_view(request):
    # Mengambil semua data task
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    # memparsing data task ke template todo/index.html dan merender nya
    return render(request, 'todo/index.html', context)

def detail_view(request, task_id):
    # Mengambil data task berdasarkan task ID
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        # Jika data task tidak ditemukan,
        # maka akan di redirect ke halaman 404 (Page not found).
        raise Http404("Task tidak ditemukan.")
    # parsing data task ke template todo/detail.html dan merendernya
    return render(request, 'todo/detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():

            new_task = TaskForm(request.POST)
            new_task.save()

            messages.success(request, 'Sukses Menambah Task baru.')
            return redirect('todo:index')
    else:
        form = TaskForm()
    return render(request,'todo/form.html',{'form': form})
def update_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Sukses Mengubah Task.')
            return redirect('todo:index')
    else:
        form = TaskForm(instance=task)
        return render(request, 'todo/form.html', {'form':form})
def delete_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request,'Sukses Menghapus Task.')
        return redirect('todo:index')
    except Task.DoesNotExist:
        raise Http404("Task tidak ditemukan.")