from django.shortcuts import render, get_object_or_404
from .models import PageCreator
from .form import PageCreatorForm


def page_creator_page(request):
    form = PageCreatorForm()
    return render(request, 'page_creator/create_page_template.html', {'form': form})


def page_creator(request, pk):
    post = get_object_or_404(PageCreator, pk=pk)
    return render(request, 'page_creator/created_page.html', {'post': post})
