from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','status')
        labels = {
            'title': _('Judul'),
            'description': _('Deskripsi'),
            'status': _('Status')
        }
        error_messages ={
            'title':{
                'required': _("Judul Harus Diisi."),
            },
            'description':{
                'required': _("Deskripsi Harus Diisi."),
            },
        }