from django.shortcuts import render
from .models import Book #[span_3](end_span)

# [span_4](start_span)المهمة 3: استعلام بسيط[span_4](end_span)
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') #[span_5](end_span)
    return render(request, 'bookmodule/bookList.html', {'books': mybooks}) #[span_6](end_span)

# [span_7](start_span)المهمة 4: استعلام معقد[span_7](end_span)
def complex_query(request):
    # [span_8](start_span)تطبيق عدة فلاتر كما هو مطلوب في لاب 7[span_8](end_span)
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10] #[span_9](end_span)
    
    if len(mybooks) >= 1: #[span_10](end_span)
        return render(request, 'bookmodule/bookList.html', {'books': mybooks}) #[span_11](end_span)
    else:
        return render(request, 'bookmodule/index.html') #[span_12](end_span)


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')