from django.urls import path
from .views import accept_friend_request, edit, dashboard, register,post, index, blogs, download,friends, create_post,send_friends_request,send_friends_request,friends,friends_accept
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

app_name = 'authapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),
    path('post/', blogs, name='post'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), 
    path('download/', download, name = "download"),
    path('friend-add/', friends, name = "friends"),
    path('friend-request', friends_accept, name = "friends_accept"),
    path('createpost/', create_post, name = "createpost"),
    path('send_friend_request/<int:userID>/',
         send_friends_request,name = 'send friend request'),
    path('accept_friend_request/<int:requestID>/',accept_friend_request,name = 'accept friend request'),
    
]
