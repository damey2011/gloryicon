from django.shortcuts import render

# Create your views here.
from django.views import View


class CuroHome(View):
    def get(self, request):
        return render(request, 'curo/index.html');