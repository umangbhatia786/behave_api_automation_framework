import random
from faker import Faker


def generate_random_book_name():
    adjectives = ['Mysterious', 'Enchanting', 'Whimsical', 'Intriguing', 'Captivating', 'Epic', 'Magical', 'Thrilling',
                  'Surreal', 'Timeless']
    nouns = ['Adventure', 'Journey', 'Quest', 'Secrets', 'Chronicles', 'Legends', 'Mysteries', 'Wonders', 'Realm',
             'Odyssey']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    book_name = f"{adjective} {noun}"
    return book_name


def generate_random_isbn():
    isbn_vals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '0', '2', '3', '4', '5', '6', '7', '8', '9']
    return ''.join(random.choice(isbn_vals) for x in range(4))


def generate_random_aisle():
    return str(random.randint(1000, 9999))


def generate_random_full_name():
    fake = Faker()
    return fake.name()
