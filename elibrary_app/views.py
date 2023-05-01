from django.shortcuts import render
from elibrary_app.forms import AddBookForm
from elibrary_app.models import Catalogue

def home(request):
    
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)

        if add_book_form.is_valid():
            add_book_form.save()

    books = Catalogue.objects.all()

    add_book_form = AddBookForm()

    return render(request, 'elibrary_app/index.html', context={'add_book_form':add_book_form, 'books':books})
