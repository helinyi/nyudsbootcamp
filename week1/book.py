books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]

# 1.Checking Book Ratings
def check_rating(book):
    if book.rating > 4.5:
        return true
    return false

def check_rating_new(book):
    if book.rating <= 4.0:
        return low
    elif book.rating <= 4.5:
        return medium
    else:
        return high

# 2.Average Rating by Genre
def average_rating_by_genre(books, genre):
    sum = 0
    count = 0
    for book in books:
        if book.genre == genre:
            sum += books.rating
            count+=1
    if count == 0:
        return -1
    return sum / count



# 3.Books by Author
def books_by_author(books, author):
    l = []
    for book in books:
        if book.author == author:
            l.append(book)
    
    if len(l) == 0:
        return null
    else:
        return l
    