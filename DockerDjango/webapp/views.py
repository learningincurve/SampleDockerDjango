from django.http import HttpResponse
from django.views import View


# Create your views here.

class FirstView(View):
    def get(self, request):
        return HttpResponse("<h1>Let's learn Django Web development<h1>")
