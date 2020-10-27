from urllib.error import URLError

from django.http import JsonResponse
from django.shortcuts import render
import urllib
from .models import TestLink


def link_view(request):
    links = TestLink.objects.all()
    context = {'links':links}
    return render(request, 'test_task/all_links.html', context)

def is_link_correct(request):
    link = request.GET.get('link')
    try:
        status = urllib.request.urlopen(link).getcode()
    except URLError:
        status = 500
    data = {'status':status}
    return JsonResponse(data)

