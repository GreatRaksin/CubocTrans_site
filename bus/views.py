from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from bus.models import Head, Contact
from .forms import UserForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class IndexView(ListView):
    context_object_name = 'index'
    template_name = 'index.html'
    queryset = Head.objects.all()

# TODO: сделать генерацию партнеров
#  Сетка из логотипов, отображается лого-ссылка
#  и название фирмы-партнера


class ContactView(FormView):
    model = Contact
    form_class = UserForm
    success_url = '/thanks'

    def form_valid(self, myform):
        myform.save()  # сохранение в БД

def contact_view(request):
    context = {'form': UserForm}
    if request.method == 'GET':
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request, 'contact.html', context)


def success_view(request):
    # TODO: сделать нормальную страницу успех
    return render(request, 'success.html')

