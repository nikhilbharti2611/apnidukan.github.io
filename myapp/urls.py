from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='loginpage'),
    path('List/', views.List, name='List'),
    path('register', views.register, name="register"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('savedata',views.savedata, name='savedata'),
    path('displaydata',views.displaydata, name='displaydata'),
    path('makeQR', views.makeQR, name="makeQR"),
    # path('qr-code/', views.qr_code, name='qr_code'),
]
