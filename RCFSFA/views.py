from django.shortcuts import render

# Create your views here.
from django.views import View


class RcfHome(View):
    def get(self, request):
        return render(request, 'RCFSFA/index.html')
