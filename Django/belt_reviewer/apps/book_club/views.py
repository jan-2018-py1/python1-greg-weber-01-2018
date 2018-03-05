from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
  
def index(req):
    # grab user from DB using session id
    user = User.objects.get(id=req.session['user_id'])
    last_3 = Review.objects.all().order_by('-id')[:3]
    # grab the id's of the books in last three reviews
    last_3_book_ids = []
    for review in last_3:
        last_3_book_ids.append(review.book.id)
    other_books = Book.objects.exclude(pk__in=list(last_3_book_ids))
    context = {
        'alias' : user.alias,
        'other_books': other_books,
        'recent_reviews': last_3
    }
    return render(req, 'book_club/user_dashboard.html', context)


def book_new(req):
    # grab set of authors from db to send to template
    content = {
        'authors' : Author.objects.all()
    }
    return render(req, 'book_club/add_book.html', content)

def review_new(req):
    # grab post info and insert new review into DB f
    book_id = req.POST['book_id']
    content = req.POST['review']
    stars = req.POST['stars']
    Review.objects.create(content=content, book=Book.objects.get(id=book_id), stars=stars, user=User.objects.get(id=req.session['user_id']))
    # make url with book id for redirect to books/<id>
    url = '/books/{}'.format(book_id)
    return redirect(url)


def book_show(req, id):
    # query spacific book info - id someone types a fake id into url this will catch it
    if Book.objects.filter(id=id).exists():
        this_book = Book.objects.get(id=id)
    else:
        return redirect('/')

    all_books = Book.objects.all()
    
    context = {
        'this_book': this_book.title,
        'book_id' :this_book.id,
        'reviews': Review.objects.filter(book=this_book),
        'all_books' : all_books,
        'user_id' : req.session['user_id']
        }

    return render(req, 'book_club/review.html', context)

def user_reviews(req, id):
    if User.objects.filter(id=id).exists():
        user = User.objects.get(id=id)
    else:
        return redirect('/')
    #number of reviews by this user
    print id 
    review_count = len(user.reviews.all())
    #this next part grabs a distinct list of book titles that the user has reviewed, allowing that the user if free to write more than one review for each book. 
    reviewed_books = Review.objects.filter(user=User.objects.get(id=id))
    reviewed_books_titles = []
    for book in reviewed_books:
        reviewed_books_titles.append(book.book.title)
    distinct_title_list = []
    for book in reviewed_books_titles:
        if book not in distinct_title_list:
            distinct_title_list.append(book)
    context = {
        'alias' : user.alias,
        'name' : '{} {}'.format(user.first_name, user.last_name),
        'email' : user.email,
        'review_count' : review_count,
        'reviewed_books':  distinct_title_list
    }
    
    return render(req, 'book_club/user_reviews.html', context)

def review_create(req):
    # grab post data from review form and insert new author into DB
    if req.POST['new_author'] != "":
        #make sure author really not in db and redirect w/ error if user error
        if len(Author.objects.filter(name=req.POST['new_author'])):
            messages.add_message(req, messages.INFO, 'The author you entered is already in the Data Base, please try your review again and select from the list')
            return redirect('/books/add')
        else:
            author =  Author.objects.create(name=req.POST['new_author'])
    else:
        author = Author.objects.get(name=req.POST['author_list'])

    # grab post data from review form and insert new book into DB
    title = req.POST['title']
    new_book = Book.objects.create(title=title, author=author)


    # grab post data from review form and insert new review into DB
    content = req.POST['review']
    stars = req.POST['stars']
    Review.objects.create(content=content, book=Book.objects.get(id=new_book.id), stars=stars, user=User.objects.get(id=req.session['user_id']))
    
    # make url with book id for redirect to books/<id>
    url = '/books/{}'.format(new_book.id)
    return redirect(url)

def review_destroy(req, id):
    if Review.objects.filter(id=id).exists():
        #delete book review and redirect
        this_review = Review.objects.get(id=id)
        this_review.delete()
    return redirect('/books')