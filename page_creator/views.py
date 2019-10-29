from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import PageCreator
from .form import PageCreatorForm


def page_creator(request, pk):
    created_page = get_object_or_404(PageCreator, pk=pk)
    return render(request, 'page_creator/created_page.html', {'created_page': created_page})


def page_creator_page(request):
    if request.method == "POST":
        form = PageCreatorForm(request.POST)

        if form.is_valid():
            created_page = form.save(commit=False)
            one_word_validate = str(created_page).split()

            # Check form for words quantity
            if len(one_word_validate) > 1 or len(one_word_validate) == 0:
                return redirect('one_word_error_page')

            created_page.save()
            return redirect('page_creator', pk=created_page.pk)
    else:
        form = PageCreatorForm()
    return render(request, 'page_creator/create_page_template.html', {'form': form})


def one_word_error_page(request):
    return render(request, 'page_creator/word_error_page.html')
