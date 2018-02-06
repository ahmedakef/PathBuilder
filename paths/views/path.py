from django.views import generic
from paths.models import Course,Path,Author
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy


class PathListView(generic.ListView):
    model = Path
    paginate_by = 10
    


class my_PathsListView(LoginRequiredMixin,PathListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = Author.objects.get(user=self.request.user)
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Path.objects.filter(creator=self.request.user)

class AuthorPathsListView(PathListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = User.objects.get(username=self.kwargs['slug']).author
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Path.objects.filter(creator=User.objects.get(username=self.kwargs['slug']))






class PathDetailView(generic.DetailView):
    model = Path

    
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = self.get_object()
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['courses'] = self.get_object().base.above.all()
        return context


#pdb.set_trace()
class PathCreate(LoginRequiredMixin,generic.CreateView):
    model = Path
    fields = ['name', 'slug', 'description','photo']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class PathUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Path
    fields = ['name', 'description','photo']

class PathDelete(UserPassesTestMixin,generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().creator

    model = Path
    success_url = reverse_lazy('paths:index')




