from mongoengine import connect
from models.quote import Quote
from models.author import Author

def search_quotes_by_author(author_name):
    author = Author.objects(fullname__icontains=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return quotes
    else:
        return []

def search_quotes_by_tag(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return quotes

def main():
    connect('My_DB_1')

    while True:
        user_input = input("Enter command: ")
        if user_input.startswith('name:'):
            author_name = user_input.split(':')[-1].strip()
            quotes = search_quotes_by_author(author_name)
            for quote in quotes:
                print(quote.quote)
        elif user_input.startswith('tag:'):
            tags = user_input.split(':')[-1].strip()
            quotes = search_quotes_by_tag(tags)
            for quote in quotes:
                print(quote.quote)
        elif user_input == 'exit':
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
