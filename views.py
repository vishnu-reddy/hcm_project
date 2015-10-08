from django.shortcuts import render_to_response,render
from .models import CornerstoneUserProfile
from .forms import CornerstoneUserProfileForm



def show_csod(request):
    manager_data = []
    if request.method == 'POST':
      form = CornerstoneUserProfileForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, "base.html", {'form': form})
    else:
       form = CornerstoneUserProfileForm()

    nodes = CornerstoneUserProfile.objects.all()
    return render(request, "base.html", {'form': form, 'nodes': nodes})
