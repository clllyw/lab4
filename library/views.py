from django.shortcuts import render_to_response
from models import Author,Book
from django.template import Context
from django.http import HttpResponse


#def show(request):    
#    book_list = Book.objects.all()   
#    c = Context({"book_list":book_list,})  
#    return render_to_response("book.html", c)
def home(request):
#    book_title_list = []
#    for b in Book.objects.all():
#        book_title_list.append(b.title)
#    c = Context({"book_title_list":book_title_list,})
    book_list = Book.objects.all()  
    c = Context({"book_list":book_list,})
    
    return render_to_response("homepage.html", c)

def retrieve(request):
    book_message = Book.objects.get(Title = request.GET["title"])
    author_message = Author.objects.filter(AuthorID = book_message.AuthorID)
    ac = Context({"author_message":author_message,})
    bc = Context({"book_message":book_message,})
    return render_to_response("book.html", ac, bc)

def search(request):
    if 'search' in request.GET and request.GET['search']:
        myauthorid = Author.objects.filter(Name = request.GET["search"])
        message = Book.objects.filter(AuthorID = myauthorid)
        search_c = Context({"book_message":message,})
        return render_to_response('author_book.html',search_c)
        #return HttpResponseRedirect('author_book.html',search_c)
    else:
        return HttpResponse('Please submit a right search term.')

def delete(request):
    message=Book.objects.get(ISBN=request.GET["ISBN"])
    message.delete()
    book_list = Book.objects.all()  
    c = Context({"book_list":book_list,})
    return render_to_response("homepage.html", c)

def update(request):
    book_message=Book.objects.get(ISBN=request.GET["ISBN"])
    bc = Context({"book_message":book_message,})
    if request.POST:
        post = request.POST
        if post["AuthorID"] and post["Publisher"] and post["PublishDate"] and post["Price"]:
            
            book_message.AuthorID = post["AuthorID"]     
            book_message.Publisher = post["Publisher"]
            book_message.PublishDate = post["PublishDate"]
            book_message.Price = post["Price"]   
            book_message.save()
        else:
            return HttpResponse('Please full all information.')
    return render_to_response("update.html",bc)

def add(request):
    if request.POST:
        post = request.POST
        if post["ISBN"] and post["Title"] and post["AuthorID"] and post["Publisher"] and post["PublishDate"] and post["Price"]:
            post = request.POST
            new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = post["AuthorID"],
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"])
            new_book.save()
        
#
#        new_author = Author(
#        AuthorID = post["AuthorID"],
#        Name = post["Name"],
#        Age = post["Age"],
#        Country = post["Country"])
#        new_author.save()
        else:
            return HttpResponse('Please full all information.')
    return render_to_response("add.html")
        

def add_author(request):
    if request.POST:
        post = request.POST
        if post["AuthorID"] and post["Name"] and post["Age"] and post["Country"]:
            new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"])
            new_author.save()
        else:
            return HttpResponse('Please full all information.')
    return render_to_response("add_author.html")