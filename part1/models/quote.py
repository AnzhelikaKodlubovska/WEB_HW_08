from mongoengine import Document, StringField, ListField, ReferenceField
from .author import Author

class Quote(Document):
    quote = StringField(required=True)
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)

    meta = {'collection': 'quotes'}  
