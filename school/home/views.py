from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from .models import Student
from .forms import Contact
from django.views.generic.base import TemplateView

# Create your views here.


class StudentListView(ListView):
    model = Student
    # template_name_suffix = "_list" #By default ye rehta h
    # template_name_suffix = '_get'
    # template_name_suffix = ''
    template_name = 'home/student_list.html'  # By default ye rehta h
    # template_name = 'home/alldata.html' #ye rkh skte h
    # context_object_name = 'student_list' #By default ye rehta h or
    # context_object_name = 'object_list' #By default ye rehta h or ye bhi
    # context_object_name = 'students'
    # ordering = ['name'] #Order kr skte h field k according

    def get_queryset(self):
        return Student.objects.filter(course='Python')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    def get_template_names(self):
        if self.request.COOKIES['name'] == 'sonam':
            template_name = 'home/sonam.html'
        else:
            template_name = self.template_name
        return [template_name]


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'home/student.html'
    # context_object_name = 'stu'
    ''' by default we can only pass either pk or slug
    If we want to use id or something else instead of pk than we have to write below code. Notice that the same variable is used in the url field.
    '''
    # pk_url_kwarg = 'id'
    # template_name_suffix = '' #we can use this also to override default _detail suffix

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_students'] = self.model.objects.all()
        return context


class ContactFormView(FormView):
    template_name = 'home/contact.html'
    form_class = Contact
    success_url = '/thankyou/'
    initial = {'name': 'Sonam'}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return redirect('/thankyou/')


class ThankYouView(TemplateView):
    template_name = "home/thankyou.html"


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thankyou/'
    template_name = 'home/studentupdate.html'

    def get_form(self):
        form = super().get_form()
        form['name'].widget = form.TextInput(attrs={'class': 'form-control'})
        form['password'].widget = form.PasswordInput(
            render_value=True, attrs={'class': 'form-control'})
        return form


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/students/'
