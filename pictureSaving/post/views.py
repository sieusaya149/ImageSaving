from django.shortcuts import render

# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        print("user is authenthicated")
        return render(request,'post/index.html')
    else:
        print("user is not authenthicated")
        return render(request,'authenthicating/login.html')
    