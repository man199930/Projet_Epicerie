from django.shortcuts import render
from importPictures.forms import FactureForm
def index(request):
    form=FactureForm()
    return render(request, 'index.html',{'form':form})
