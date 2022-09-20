from django.urls import path
from architecture import views


urlpatterns = [
    path('', views.homeView, name='index'),
    path('aboutus/', views.AboutusView, name='aboutus'),
    path('contact/', views.contactView, name='contact'),
    path('myprojects/', views.myprojectsView, name='myprojects'),
    path('detail/<int:pk>', views.DetailView.as_view(), name="detail"),
   
]