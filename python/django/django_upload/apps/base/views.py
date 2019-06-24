"""Views for the base app"""

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import UploadForm


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            download_url = form.save()
            context = {
                'download_url': download_url,
                'form': form,
            }
            return render(request, 'base/upload.html', context)
    else:
        form = UploadForm()
    return render(request, 'base/upload.html', {'form': form})
