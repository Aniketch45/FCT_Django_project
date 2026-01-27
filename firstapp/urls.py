from django.urls import path
from firstapp import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('home2/',views.home2,name='home2'),
    path('insert/',views.addstud,name='insert'),   
    path('update/<int:myid>',views.updatestud,name='update'),  
    path('delete/<int:myid>',views.deletestud,name='delete'),   
    path('forms/',views.showforms,name='forms'),
    path('insertstud/',views.insertstud,name='insertstud'),
    path('update2/<int:sid>',views.update,name='update2'),
]