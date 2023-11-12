import pika 
import uuid
from ast import literal_eval
from networkInfo import NetworkInfo
import ipaddress  
from jobs.serpent_creator import SerpentCreator
from jobs.ecdsa_creator import ECDSACreator
class RpcClient(NetworkInfo):
    def __init__(self,default_queue='galaxy'):
        super().__init__()
        self.default_queue = default_queue
        self.user_input(self.default_queue)
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
        self.call()

    def check_validate_it(self,ip):
        try:
            ip_ = ipaddress.ip_address(ip)
            print("Your IP Adrress is Valid!!")
        except ValueError:
            print("You Enter wrong IP XXX")
           
            
    def user_input(self,default_queue):
        plain_text=""
        if default_queue == 'ecdsa':
            self.ecdsa = ECDSACreator(self.users) 
            self.users = self.ecdsa.user_input()
        elif default_queue == 'serpent':
            self.serpent = SerpentCreator(self.users)
            self.users = self.serpent.user_input()

    def on_response(self,ch, method , props,body):
        if self.corr_id == props.correlation_id:
            # body = literal_eval(body.decode('utf-8'))
            # self.response = body
            if self.default_queue == 'serpent':
                self.serpent.format_serpent_output(body)
            else:
                exit()

    def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=self.default_queue,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(self.users))
        self.connection.process_data_events(time_limit=None)
        return self.response

