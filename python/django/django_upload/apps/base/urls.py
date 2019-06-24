"""urlconf for the base application"""

from django.conf.urls import url

from .views import home
from .views import upload_file


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'upload_form$', upload_file, name='upload_form'),
]
