from ast import literal_eval


class SerpentCreator:
    
    def __init__(self,user):
        self.users = user

    def user_input(self):
        plain_text=""
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
        return self.users
 
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
                
    def format_serpent_output(self,message):
        body = literal_eval(message.decode('utf-8'))
        if body[0][0] == '-p':
            print(body[0][1])
        else:
            print(body)

        
