from django.shortcuts import render


# Create your views here.
# dashboard views
def SM_dashboard(request):
    return render(request, 'dashboard/salesmanager-dashboard.html')


