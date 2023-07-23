from django.shortcuts import render

# Create your
def index(request):
    return render(request, 'index.html', {})