from django.views import generic
from paths.models import Course,Path,Author
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from paths.forms import CourseForm


class CourseListView(generic.ListView):
    model = Course
    paginate_by = 10


class CourseDetailView(generic.DetailView):
    model = Course
    
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = self.get_object()
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)


class my_CoursesListView(LoginRequiredMixin,CourseListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = Author.objects.get(user=self.request.user)
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)

    def get_queryset(self):
       return Course.objects.filter(creator=self.request.user)

class AuthorCoursesListView(LoginRequiredMixin,CourseListView):
    def get_context_data(self,**kwargs):
        # edit access counter of the object 
        object = User.objects.get(username=self.kwargs['slug']).author
        object.access_counter +=1
        object.save()
        # Call the base implementation first to get the context
        return  super().get_context_data(**kwargs)


    def get_queryset(self):
       return Course.objects.filter(creator=User.objects.get(username=self.kwargs['slug']))



#pdb.set_trace()
class CourseCreate(LoginRequiredMixin,generic.CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CourseCreateForPath(CourseCreate):
    def get_context_data(self, **kwargs):
        path = Path.objects.get(slug = self.kwargs['slug'] )
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        context['form'].initial['path'] = path
        context['form'].fields['path'].disabled= True
        context['form'].fields['depend_on'].queryset = Course.objects.filter(path=path)
        return context


class CourseUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Course
    form_class = CourseForm

class CourseDelete(UserPassesTestMixin,generic.DeleteView):
    def test_func(self):
        return self.request.user == self.get_object().creator

    model = Course
    success_url = reverse_lazy('paths:index')
