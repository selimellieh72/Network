from django.forms import ModelForm, Textarea
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['text']
        labels = {
            'text': 'Write post (Max: 256 Chr:)'
        }
        widgets = {
            'text': Textarea(attrs={'maxlength': '256', 'placeholder': 'How are you fellow networkers?'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
