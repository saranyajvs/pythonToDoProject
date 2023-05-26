from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import tasks
from .todoForm import todoFrom
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.
class TaskListView(ListView):
    model = tasks
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetailview(DetailView):
    model = tasks
    template_name = 'detail.html'
    context_object_name = 'tasks1'

class TaskUpdateview(UpdateView):
    model = tasks
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority', 'date')

    def get_success_url(self):
        return reverse_lazy ('cbvDetails',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = tasks
    template_name = 'deleteTask.html'
    success_url = reverse_lazy('cbvHome')

def addTasks(request):

    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task1 = tasks(name=name, priority=priority,date=date)
        task1.save()
    task = tasks.objects.all()
    return render(request, 'home.html', {'tasks1': task})


def deleteTask(request, taskId):
    task = tasks.objects.get(id=taskId)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'deleteTask.html')


def update(request, taskId):
    task1 = tasks.objects.get(id=taskId)
    form1 = todoFrom(request.POST or None, instance=task1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, 'edit.html', {'edtask': task1, 'edform': form1})


def details(request):
    task = tasks.objects.all()
    return render(request, 'detail.html', {'tasks1': task})
