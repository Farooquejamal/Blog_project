from django import forms
from .models import BlogModel, Category, Comment

# Get all categories for the dropdown
# choices = Category.objects.all().values_list('name', 'name').distinct()
# choice_list = [item for item in choices]


class YourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = Category.objects.all()
        self.fields['category_field'].choices = [(item.id, item.name) for item in choices]



class PostForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'title_tag', 'content', 'slug','author', 'category','snippet', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','id':'elder','type':'hidden'}),
            
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically populate the choices for the category field
        self.fields['category'].widget = forms.Select(
            choices=[(item.id, item.name) for item in Category.objects.all()],
            attrs={'class': 'form-control'}
        )



class UpdateForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'title_tag', 'content', 'slug', 'image','snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
