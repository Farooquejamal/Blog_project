from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.views.generic import DetailView,CreateView
from home.models import Profile


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        response =  super().form_valid(form)
        return response

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','facebook_url','instagram_url','twitter_url']
    success_url = reverse_lazy('home')

# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'

#     def get_context_data(self,*args,**kwargs):
#         # users = Profile.objects.all()
#         context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
#         page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

#         context["page_user"] = page_user
#         return context


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        
        # Access the object directly using self.object, which is set by DetailView
        page_user = self.object
        
        # Add the page_user to the context
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

def password_success(request):
    return render(request,'registration/password_success.html',{})

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    


