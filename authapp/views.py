from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm,PostForm
from django.views import generic
from .models import Post,Friend_Request
from django.contrib.auth.models import User



# Create your views here.

def friends(request):
    users = User.objects.all()
    return render(request, 'authapp/friendrequest.html', {'allusers':users})
def friends_accept(request):
    all_friend_requests = Friend_Request.objects.all()
    current_user = request.user
    to_user = User.objects.get(id = current_user.id)
    all_friend_requests = Friend_Request.objects.filter(to_user = to_user)
    
    return render(request, 'authapp/friends_request.html', {'all_friend_requests':all_friend_requests})
def download(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'authapp/download.html', context=context)
    
def index(request):
    queryset = Post.objects.all()    
    context= {'post': queryset}
    return render(request, "authapp/post.html", context)
def blogs(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-created_on')
    return render(request, "authapp/post.html", {'posts':posts})
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'authapp/post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'authapp/post_detail.html'
@login_required
def send_friends_request(request,userID):
    from_user = request.user
    to_user = User.objects.get(id = userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user = from_user, to_user = to_user)
    if created:
        return HttpResponse('frined request sent')
    else:
        return HttpResponse('friend request was already sent')
@login_required
def accept_friend_request(request,requestID):
    friend_request = Friend_Request.objects.get(id = requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('frind request not accepted')
        
@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'authapp/dashboard.html', context=context)

def post(request):
    context = {
        "welcome": "Welcome to posts"
    }
    return render(request, 'authapp/post.html', context=context)

def friend(request):
    context = {
        "welcome": "Friend Requests"
    }
    return render(request, 'authapp/friendrequest.html', context=context)



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()
            return render(request, 'authapp/postcreated.html')
    else:
        form = PostForm()

    context = {
        "form": form
    }

    return render(request, 'authapp/make_post.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)

