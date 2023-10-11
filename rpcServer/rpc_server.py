import pika
from ast import literal_eval
from jobs.serpent import Serpent

class RpcServer:
    def __init__(self,default_queue=''):
        super().__init__()
        self.default_queue = default_queue
        self.service = {}
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.default_queue)
        self.lanuch_service()
        self.prompt_init()
        
    def lanuch_service(self):
        if self.default_queue == 'serpent':
            self.service = Serpent()
        elif self.default_queue == 'galaxy':
            print("NONE")


    def check_client_info(self,client_info):
        print(client_info)
        client_info = literal_eval(client_info.decode('utf-8'))
        if (client_info['ip'] is not None) and \
        (client_info['hostname'] is not None):
           return True
        else: return False

    def on_request(self,ch,method,props,body):
        client_info_flag = self.check_client_info(body)
        if client_info_flag is True:
            self.service.get_nic_name(body)
            response=self.default_queue
            ch.basic_publish(exchange='',
            routing_key=props.reply_to,
            properties = pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            raise Exception("this Client not authorized!!!")

    def prompt_init(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.default_queue,on_message_callback=self.on_request)
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
