from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#
# def v_start_page(request):
#     return HttpResponse("Hello, world!")
#
#
def v_about(request):
    return render(request, "wait_list_app/moselg_1.html")

def v_start_page(request):
    return render(request, "wait_list_app/base.html")

