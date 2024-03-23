import pika

class RabbitMQClient:
    def __init__(self, host='localhost'):
        self.host = host
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, queue_name, message):
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.channel = None
