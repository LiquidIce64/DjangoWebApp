def average_rating(rating_list):
    if not rating_list: return 0
    return round(sum(rating_list) / len(rating_list))


def get_book_details(book):
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        number_of_reviews = len(reviews)
    else:
        book_rating = None
        number_of_reviews = 0
    return {
        'book': book,
        'rating': book_rating,
        'number_of_reviews': number_of_reviews
    }
