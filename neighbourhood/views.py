from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Business,Post,Comments,NeighbourHood
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.
@login_required(login_url='accounts/login/')
def dashboard(request):
    post = Post.objects.all()
    
    #adding context
    post = {'post':post}
    return render(request,'dashboard.html', post)

def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("project")
        searched_category = NeighbourHood.search_neighbourhood(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for anything yet"
        return render(request, 'search.html',{"message":message})