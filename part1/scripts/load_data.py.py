from mongoengine import connect
import json
from models.author import Author
from models.quote import Quote

def load_authors_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author(
                fullname=author_data['fullname'],
                born_date=author_data['born_date'],
                born_location=author_data['born_location'],
                description=author_data['description']
            )
            author.save()

def load_quotes_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data['author']
            author = Author.objects(fullname=author_name).first()
            if author:
                quote = Quote(
                    quote=quote_data['quote'],
                    tags=quote_data.get('tags', []),
                    author=author
                )
                quote.save()

def main():
    connect('My_DB_1')
    load_authors_from_json('data/authors.json')
    load_quotes_from_json('data/quotes.json')

if __name__ == "__main__":
    main()
