from django.shortcuts import render

def home(request):
    data = None

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "message": request.POST.get("message"),
        }

    return render(request, "home.html", {"data": data})
