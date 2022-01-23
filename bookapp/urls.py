from .views import Home
from django.urls import path, include
from .views import AllBooks, CreateBook, UpdateBook, DeleteBook, BookDetail, CustomLoginView, SignupView, ConfirmLogoutView, CustomLogoutView

urlpatterns = [
    path('', Home.as_view(), name ='home'),
    path('all/',AllBooks.as_view(), name='all-books'),
    path('detail/<int:pk>/',BookDetail.as_view(), name='book-detail'),
    path('create/',CreateBook.as_view(), name='create'),
    path('update/<int:pk>/',UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>/',DeleteBook.as_view(), name='delete'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('signup/',SignupView.as_view(), name='signup'),
    path('logout-confirm/',ConfirmLogoutView.as_view(), name='logout-confirm'),
    path('logout/',CustomLogoutView.as_view(), name='logout'),
    path('api/',include(('bookapp.api.urls','bookapp'),namespace='book-api'), name='book-api'),
    ]
