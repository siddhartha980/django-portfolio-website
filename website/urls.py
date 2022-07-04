from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('contact/',views.contact, name='contact'),
    path('contactus/',views.contactus, name='contactus'),
    path('mycv/',views.mycv, name='mycv'),
    path('research/',views.research, name='research'),

]