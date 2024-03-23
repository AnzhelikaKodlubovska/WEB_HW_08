import pika
import json
from models.contact import Contact

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')


def callback(ch, method, properties, body):
    contact_id = json.loads(body.decode())['contact_id']
    print(" [x] Received %r" % contact_id)

    contact = Contact.objects(id=contact_id).first()
    if contact:
        contact.email_sent = True
        contact.save()


channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
