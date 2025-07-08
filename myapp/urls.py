from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('speakers/', views.speakers, name='speakers'),
    path('schedule/', views.schedule, name='schedule'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('ticket-form/', views.ticket_form, name='ticket-form'),
    path('ticket-success/', views.ticket_success,name='ticket-success'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('change-password/', views.change_password, name='change-password'),
    

]
