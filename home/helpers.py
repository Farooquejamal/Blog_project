from django.utils.text import slugify
from .models import *
import string
import random

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase+string.digits,k=N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text + generate_random_string(5))
    return new_slug