from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    # path('menu-items/', views.MenuItemView.as_view(), name='menu-items'),
    # path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('book/', views.book, name='book'),
    path('tables/', views.BookingViewSet.as_view({'get' : 'list'})),
]
