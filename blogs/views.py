from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogs.forms import BlogForm
from blogs.models import Blog
from client.models import Client
from mailing.models import Mailing


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blogs')

    def form_valid(self, form):
        mailing = form.save()
        mailing.user = self.request.user
        mailing.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'image',)
    success_url = reverse_lazy('blogs:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blogs')


def main(request):
    client = len(Client.objects.all().distinct('email'))
    blog = Blog.objects.filter(is_published=True).order_by('?')
    mailing = len(Mailing.objects.all())
    mailing_active = len(Mailing.objects.filter(status=2))
    context = {
        'blog': blog[:3],
        'mailing': mailing,
        'mailing_active': mailing_active,
        'client': client
    }
    return render(request, 'blogs/main.html', context)
