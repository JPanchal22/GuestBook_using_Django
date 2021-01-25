from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Comment
from .forms import commentForm

# Create your views here.
def index(request):
    comments = Comment.objects.order_by("-date")

    return render(request, "Guestbook/index.html", {"comments":comments})

def comment(request):
    if request.method == "POST": 
        comment_form = commentForm(request.POST)

        if comment_form.is_valid():
            new_comment_details = Comment(name=request.POST["name"], comment=request.POST["comment"])
            new_comment_details.save()
            return redirect("index")

    else:
        comment_form = commentForm()
    
    return render(request, "Guestbook/comment_form.html", {"comment_form":comment_form})