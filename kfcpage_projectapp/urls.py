from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('signin/', views.signin, name='signin'),
    path('signin/signup/', views.signup, name='signup'),
    path('menu/signin/', views.signin, name='signin'),
    path('menu/orders1/<int:id>', views.orders1, name='orders1'),
    path('menu/orders2/<int:id>', views.orders2, name='orders2'),
    path('menu/orders3/<int:id>', views.orders3, name='orders3'),
    path('menu/orders4/<int:id>', views.orders4, name='orders4'),
    path('menu/orders5/<int:id>', views.orders5, name='orders5'),
    path('menu/orders6/<int:id>', views.orders6, name='orders6'),
    path('menu/orders7/<int:id>', views.orders7, name='orders7'),
    path('menu/orders8/<int:id>', views.orders8, name='orders8'),

    path('abc/', views.abc, name='abc'),


]