def get_add_book_payload(book_name, isbn_val, aisle_val, author_name):
    payload_json = {
        "name": book_name,
        "isbn": isbn_val,
        "aisle": str(aisle_val),
        "author": author_name
    }

    return payload_json


def get_delete_book_payload(book_id):
    payload_json = {
        "ID": book_id
    }

    return payload_json


def get_book_by_id_params(book_id):
    return {'ID': book_id}


def get_book_by_author_params(author_name):
    return {'AuthorName': author_name}