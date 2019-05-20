from django.shortcuts import render
from .models import Users

# Create your views here.
def index(request):
    utilizatori = Users.objects.all()
    return render(request, 'core/index.html', {'utilizatori':utilizatori})