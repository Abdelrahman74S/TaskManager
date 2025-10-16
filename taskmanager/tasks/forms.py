from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'status', 'category']
        
class updateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'status', 'category']
    