import json
import random

from faker import Faker
from random import randint, uniform
from conf import models

# Fields
# 1. Title
with open("books.txt") as f:
    books = f.read().splitlines()


def title() -> str:
    return books[randint(0, 4)]


# 2. Year
def year() -> int:
    return randint(2010, 2021)


# 3. Pages
def pages() -> int:
    return randint(100, 500)


# 4. ISBN
def isbn_13() -> str():
    fake = Faker()
    Faker.seed(0)
    return fake.isbn13()


# 5. Rating
def rating() -> float:
    return uniform(1, 5)


# 6. Price
def price() -> float:
    return uniform(10, 500)


# 7. Author
def author() -> list:
    return [f"test_author{i}" for i in range(1, randint(2, 4))]

# Create dict of one book
def book_dict(pk=1) -> dict:
    book = {
        "model": models[randint(0, 7)],
        "pk": pk,
        "fields": {
            "title": title(),
            "year": year(),
            "pages": pages(),
            "isbn13": isbn_13(),
            "rating": rating(),
            "price": price(),
            "author": author()
        }
    }

    return book


def write_json(data: list):
    with open("output.txt", 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
        outfile.write('\n')


def main():
    books_list = []
    for pk in range(1, 101):
        books_list.append(book_dict(pk))
    write_json(books_list)


if __name__ == "__main__":
    main()
