from django.shortcuts import render

# Create your views here.
def home(request):
    """Displays the index page."""
    template = 'index.html'
    return render(request, template)