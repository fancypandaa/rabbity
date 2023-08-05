import pika 
import uuid
from ast import literal_eval
from networkInfo import NetworkInfo
class RpcClient(NetworkInfo):
    def __init__(self):
        super().__init__()
        self.connection= pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='',exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )
        self.response = None
        self.corr_id = None
    
    def on_response(self,ch, method , props,body):
        if self.corr_id == props.correlation_id:
            print(body)
            body = literal_eval(body.decode('utf-8'))
            self.response = body

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='aot',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),body=str(self.users))
        self.connection.process_data_events(time_limit=None)
        return self.response
