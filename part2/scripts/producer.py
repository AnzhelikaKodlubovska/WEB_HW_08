import pika
import json
from models.contact import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')


def publish_message(body):
    channel.basic_publish(exchange='', routing_key='email_queue', body=body)
    print(" [x] Sent %r" % body)


def main():
    contacts = Contact.objects[:10] 
    for contact in contacts:
        message = json.dumps({'contact_id': str(contact.id)})
        publish_message(message)

    connection.close()


if __name__ == '__main__':
    main()
