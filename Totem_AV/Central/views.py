from django.shortcuts import render

# Create your views here.
def Principal(request):
    return render(request,'Central/HTML/Principal.html')