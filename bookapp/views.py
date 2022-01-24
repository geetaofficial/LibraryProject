from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from .forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Home(TemplateView):
    """Home Template View"""
    template_name = 'home.html'


class AllBooks(LoginRequiredMixin, ListView):
    """Book List View"""
    template_name = 'book_list.html'
    model = Book


class BookDetail(LoginRequiredMixin, DetailView):
    """Book Detail View"""
    template_name = 'book_detail.html'
    model = Book


class CreateBook(LoginRequiredMixin, CreateView):
    """Book Create View"""
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    # success_url=reverse_lazy('all-books')


class UpdateBook(LoginRequiredMixin, UpdateView):
    """Book Update View"""
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('all-books')


class DeleteBook(DeleteView):
    """Book Delete View"""
    model = Book
    fields = '__all__'
    template_name = 'book_del.html'
    success_url = reverse_lazy('all-books')


class CustomLoginView(LoginView):
    """User Custom Login View"""
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    """User Logout View"""
    pass


class SignupView(CreateView):
    """User Sign-up View"""
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')


class ConfirmLogoutView(TemplateView):
    """User Logout View"""
    template_name = 'logout_confirm.html'
