from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import User

# Create your views here.
def index(request):
    user_list = User.objects.order_by("-pub_date")
    context = {
        "user_list" : user_list
    }
    return render(request, "UserListApp/index.html", context)

def add(request):
    try:
        # On the first time this page loads, the request is not a POST
        # and we get an exception
        new_user = User(user=request.POST["username"], pub_date=timezone.now())
    except Exception as e:
        # Redisplay the question voting form.
        return render(
            request,
            "UserListApp/add.html",
            {
                "error_message": str(e),
            },
        )
    else:
        new_user.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("UserListApp:index", args=()))
