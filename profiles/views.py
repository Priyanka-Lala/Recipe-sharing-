from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Profile
from .forms import Profileform


# Create your views here.



class Profiles(TemplateView):
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {
            'profile': profile,
            'form':Profileform(instance=profile)
                   }
        return context



class Editprofile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = Profileform
    model = Profile

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)


    def test_func(self):
          return self.request.user == self.get_object().user
