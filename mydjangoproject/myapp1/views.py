from django.shortcuts import render

from myapp1.models import Worker


def index_page(request):

    my_dictionary = {'data': 'lists', 'data2': 'hi'}

    all_workers = Worker.objects.all()

    return render(request, 'index.html', {'data': all_workers})

def about(request):
    return render(request, 'about.html')