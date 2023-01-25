from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render 
from .models import Restaurant, Comment 
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(location=self.kwargs['location'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = self.kwargs['location']
        return context

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = ['name', 'location', 'website', 'address', 'price_range', 'type', 'hours', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['name', 'location', 'website', 'address', 'price_range', 'type', 'hours', 'image']
    success_url = '/'

class RestaurantDelete(DeleteView):
    model = Restaurant 
    sucess_url = '/'
    
class CommentCreate(CreateView):
    model = Comment
    fields = ['comment', 'rating']

#for the detail class in order to get it to work, the comments model will need to have the foreign key! I can always adjust accordingly once the models are created if there are any bugs :)
class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'
    context_object_name = 'restaurant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

