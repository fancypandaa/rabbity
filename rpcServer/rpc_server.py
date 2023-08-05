import pika
from ast import literal_eval
from channels import Channels
class RpcServer(Channels):
    def __init__(self):
        super().__init__()
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        for i in self.default_queue:
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=i)

    def check_client_info(self,client_info):
        client_info = literal_eval(client_info.decode('utf-8'))
        if (client_info['ip'] is not None) and \
        (client_info['hostname'] is not None):
           return True
        else: return False

    def on_request(self,ch,method,props,body):
        queue=method.routing_key
        client_info_flag = self.check_client_info(body)
        if client_info_flag is True:
            response=self.default_queue
            ch.basic_publish(exchange='',
            routing_key=props.reply_to,
            properties = pika.BasicProperties(correlation_id=props.correlation_id),
            body=str(response))
            self.update_channel(queue)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            raise Exception("this Client not authorized!!!")

    def prompt_init(self,queue):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue,on_message_callback=self.on_request)
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
