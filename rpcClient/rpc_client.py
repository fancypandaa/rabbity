import pika 
import uuid
from ast import literal_eval
from networkInfo import NetworkInfo
import ipaddress  

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

    def check_plain_text_length(plain_text):
        x = plain_text.spilt()
        number_of_words= len(x)
        return number_of_words
    def user_input(self,default_queue):
        if default_queue == 'galaxy':
            print("Enter URI you want find it? ")
            s = input()
        elif default_queue == 'serpent':
            option= input("Choose Encrption or Decrption: e/D")
            if option.lower() == "e" or option.lower() == "d":
                self.users["option"] = option
            else:
                print("Wrong option, No comments.....")
                exit()
            
            print("Enter your message and don't exceed 100 words!!")
            s = input()
            number_of_words=self.check_plain_text_length(s)
            if number_of_words <= 100:
                self.users["plain_text"]= s
                print(f'{}/100 accepted length...')
                user_key_option= input("choose auto generate key: y/N")
                if user_key_option == "y":
                    self.users["users_key_option"]=True
                elif user_key_option == "N":
                    user_key = input("Enter Your Key between 128bit and 256bit")
                    self.users["user_key"]= user_key
            else:
                print(f'{}/100 exceed limit FUCK YOU...')
                exit()

            
            

    def on_response(self,ch, method , props,body):
        if self.corr_id == props.correlation_id:
            body = literal_eval(body.decode('utf-8'))
            self.response = body


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

