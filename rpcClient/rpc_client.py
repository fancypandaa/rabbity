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

    def check_plain_text_length(self,plain_text):
        x = plain_text.split()
        number_of_words= len(x)
        return number_of_words

    def check_cipher_text(self,cipher_text):
        p = set(cipher_text)
        s= {'0','1'}
        if s == p or p == {'0'} or p == {'1'}:
            return True
        else:
            return False
    
    def _serpent_encrypt_builder(self):
            print("Enter your message between 5 to 100 words!!")
            plain_text = input()
            number_of_words= self.check_plain_text_length(plain_text)
            if number_of_words >= 5 and number_of_words <= 100:
                self.users["plain_text"]= plain_text
                print(f'{number_of_words}/100 accepted length...')
                user_key_option= input("choose auto generate key: y/N: ")
                if user_key_option.lower() == "y":
                    self.users["auto_generate_key"]=True
                elif user_key_option.lower() == "n":
                    user_key = input("Enter Your Key between 128bit and 256bit")
                    self.users["auto_generate_key"]=False
                    self.users["user_key"]= user_key
                else:
                    print("FUCK OFF!!!")
            else:
                print(f'{number_of_words}/100 exceed limit FUCK YOU...')
                exit()
    
    def _serpent_decrypt_builder(self):
            print("Enter your Cipher")
            cipher_text = input()
            if self.check_cipher_text(cipher_text):
                self.users["cipher_text"]= cipher_text
                user_key = input("Enter Your Key between 128bit and 256bit\n")
                self.users["auto_generate_key"]=False
                self.users["user_key"]= user_key
            else:
                print(f'wrong format FUCK YOU...')
                exit()

    def user_input(self,default_queue):
        plain_text=""
        if default_queue == 'galaxy':
            print("Enter URI you want find it? ")
            s = input()
        elif default_queue == 'serpent':
            option= input("Choose Encrption or Decrption: e/D: ")
            if option.lower() == "e" :
                self.users["option"] = "-"+option.lower()
                self._serpent_encrypt_builder()
            elif option.lower() == "d":
                self.users["option"] = "-"+option.lower()
                self._serpent_decrypt_builder()
            else:
                print("Wrong option, No comments.....")
                exit()
            # print(self.users)
            
            
            

    def on_response(self,ch, method , props,body):
        if self.corr_id == props.correlation_id:
            body = literal_eval(body.decode('utf-8'))
            self.response = body
            print(self.response[0][1].decode('utf-8'))


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

