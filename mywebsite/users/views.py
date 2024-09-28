from django.shortcuts import render, HttpResponse

# Create your views here.

def profile_view(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'users/user_profile.html', context)