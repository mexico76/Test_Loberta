from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import link_view, is_link_correct

urlpatterns = [
    path('', login_required(link_view), name='urls'),
    path('ajax/check_link', is_link_correct, name='correct_link'),
]
