import pika
from ast import literal_eval
from jobs.serpent.test_serpent import Serpent
from jobs.ecdsa.ecDSA import ECDSA
class RpcServer:
    def __init__(self,default_queue=''):
        super().__init__()
        self.default_queue = default_queue
        self.serpent = {}
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.default_queue)
        self.lanuch_service()
        self.prompt_init()
        
    def lanuch_service(self):
        if self.default_queue == 'serpent':
            self.serpent = Serpent()
        elif self.default_queue == 'ecdsa':
            self.ecdsa = ECDSA()
        else:
            exit()  

    def check_client_info(self,client_info):
        client_info = literal_eval(client_info.decode('utf-8'))
        if (client_info['ip'] is not None) and \
        (client_info['hostname'] is not None):
           return True
        else: return False
    def extract_method_data_ecdsa(self,body):
        options = []
        body = literal_eval(body.decode('utf-8'))
        print(body)
        if body['option'] == '-s':
            message = body['message']
            options.append("s")
            options.append(message)
        elif body['option'] == '-v':
            options.append("v")
            options.append(body["publicKey"])
            options.append(body["signature"][0])
            options.append(body["signature"][1])
            options.append(body["message"])
        else:
            print("FUck OFF!!")
            exit()
        return options
            
    def extract_method_data_serpent(self,body):
        options = []
        body = literal_eval(body.decode('utf-8'))
        print(body)
        if body['option'] == '-e':
            encrypt= (body['option'],'')
            options.append(encrypt)
            if (body['auto_generate_key'] == False) and (body['user_key']):
                options.append(('-k',body['user_key']))

            if body['plain_text']:
                options.append(('-p',body['plain_text']))
            else: 
                exit()
            
            
        elif body['option'] == '-d':
            decrypt = (body['option'],'')
            options.append(decrypt)
            if body['cipher_text']:
                options.append(('-c',body['cipher_text']))
            else:
                exit()
            if body['user_key']:
                options.append(('-k',body['user_key']))     
            else:
                exit() 
        return options  

    def on_request(self,ch,method,props,body):
        client_info_flag = self.check_client_info(body)
        if client_info_flag is True:
            opts={}
            if self.default_queue == 'serpent':
                opts=self.extract_method_data_serpent(body)
                response= self.serpent.main(opts,[])

            elif self.default_queue == 'ecdsa':
                opts=self.extract_method_data_ecdsa(body)
                response=self.ecdsa.main(opts)
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
        print(" [x] Server on fire |:^_^:|")
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
