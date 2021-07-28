from django.shortcuts import render
from . models import Image
from .forms import ImageForm
# Create your views here.


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
        image = Image.objects.all()
    return render(request, 'myapp/home.html', {'form': form, 'image': image})
