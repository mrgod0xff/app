from django.shortcuts import render

# Create your views here.
def photos(request):
    template_name = 'galerie/galerie.html'
    return render(request, template_name)