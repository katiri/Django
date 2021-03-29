from django.urls import path
from .views import *

urlpatterns = [
    path('', IniciandoDjango.as_view(), name='IniciandoDjango'),
    path('class/', ClassView.as_view(), name='ClassIndex'),
    path('def/', DefView, name='DefIndex'),
    path('git/', Git.as_view(), name='ComandosGit'),
]