from django.shortcuts import render,redirect

sk=""
# Create your views here.
def index(request):
    global sk
    if 'searchKeyword' in request.GET:
        sk = request.GET['searchKeyword']
        return redirect("browse.html")
    return render(request, "index.html")
def browse(request):
    global sk
    if 'searchKeyword'not in request.GET:
        sk = ""
    print(sk)
    return render(request, "browse.html")
def details(request):
    global sk
    if 'searchKeyword' in request.GET:
        sk = request.GET['searchKeyword']
        return redirect("browse.html")
    return render(request, "details.html")
def streams(request):
    global sk
    if 'searchKeyword' in request.GET:
        sk = request.GET['searchKeyword']
        return redirect("browse.html")
    return render(request, "streams.html")
def profile(request):
    global sk
    if 'searchKeyword' in request.GET:
        sk = request.GET['searchKeyword']
        return redirect("browse.html")
    return render(request, "profile.html")
def registration(request):
    
    return render(request, "registration.html")