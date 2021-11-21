from django.shortcuts import render
from Utils.decorator import login_required

@login_required
def home(request):
    
    context = {
        'usuario': request.user,
        'status': request.GET.get('status')
    }
    
    return render(request, 'home.html', context)