from django.shortcuts import render
from .forms import index_form
from .models import TemplateImages

# Create your views here.
def home_view(request):
    ios = TemplateImages.ios_img
    return render(request, 'DevOneApp/index.html', {})
