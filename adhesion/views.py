from django.shortcuts import render

# Create your views here.

def addUser(request):
    template_name = 'adhesion/adherant.html'
    return render(request, template_name)