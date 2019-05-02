# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Running Locally!')

