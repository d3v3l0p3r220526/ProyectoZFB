from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [ 'documentId','empresa', 'nombres', 'apellidos', 'date_ini', 'date_end', 'important']
