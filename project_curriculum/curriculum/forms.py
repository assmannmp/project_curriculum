from django.forms import ModelForm
from .models import Curriculum


class CurriculumForm(ModelForm):
    class Meta:
        model = Curriculum
        fields = ['curriculum','first_name','last_name','email', 'linkedIn','title_the_presentation_letter','presentation_letter']

