from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.shortcuts import render 
from .models import Restaurant, Comment 
=======
from .models import Restaurant, Comment, User
>>>>>>> 304d30c (changes to html files, views and forms)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'error_message': 'Invalid sign up - try again'})


class Home(TemplateView):
    template_name = 'home.html'
    

class About(TemplateView):
    template_name = 'about.html'


class RestaurantsIndex(ListView):
    model = Restaurant
    template_name = 'restaurants/index.html'
    
<<<<<<< HEAD
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(location=self.kwargs['location'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = self.kwargs['location']
=======
    def get_queryset(self):
        return self.model.objects.filter(location='NY')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'NY'
        return context
    
class RestaurantsMAIndex(ListView):
    model = Restaurant
    template_name = 'restaurants/index.html'
    
    def get_queryset(self):
        return self.model.objects.filter(location='MA')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'MA'
>>>>>>> 304d30c (changes to html files, views and forms)
        return context


class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class RestaurantUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Restaurant
    fields = ['name', 'location', 'website', 'address', 'price_range', 'type', 'hours', 'image']

    def test_func(self):
        restaurant = self.get_object()
        return restaurant.user == self.request.user

    def handle_no_permission(self):
        return redirect(reverse('home'))

    def get_success_url(self):
        return reverse('detail', args=[self.object.location, self.object.pk])


class RestaurantDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    raise_exception = False

    def test_func(self):
        restaurant = self.get_object()
        return restaurant.user == self.request.user

    def handle_no_permission(self):
        return redirect(reverse('home'))
    
    def get_success_url(self):
        return reverse('restaurants', args=[self.object.location])

    
class CommentCreate(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = Comment
    fields = ['comment', 'rating']

class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
