import os

from django.http import HttpResponse
from django.shortcuts import render

from .utils import update_github_io

# Create your views here.
def default(request):
    path = os.path.join('.', 'test_dir')
    url = 'https://github.com/rlworkgroup/dowel.git'
    try:
        update_github_io(path, url)
        return HttpResponse('Updated local!')
    except Exception:
        return HttpResponse('Failed to update local!')
