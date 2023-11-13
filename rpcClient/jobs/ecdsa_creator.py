from ast import literal_eval


class ECDSACreator:
    
    def __init__(self,user):
        self.users = user

    def user_input(self):
        print(":OLO")
        plain_text=""
        option= input("Create Signature or Verify: s/V: ")
        if option.lower() == "s" :
            self.users["option"] = "-"+option.lower()
            self._signature_()
        elif option.lower() == "v":
            self.users["option"] = "-"+option.lower()
            self._verification_builder()
        else:
            print("Wrong option, No comments.....")
            exit()
            # print(self.users)
        return self.users
    def check_key_length(self,key):
        x = x.split()
        return len(x)
    
    def check_plain_text_length(self,plain_text):
        x = plain_text.split()
        number_of_words= len(x)
        return number_of_words
    def check_bytes_info(self,text):
        if text[0] == 'b' and text [1] == "'":
            text = text.replace("b", "")
            text = text.replace("'", "")
        return text
    
    def _signature_(self):
            print("Enter your message between 5 to 100 words!!")
            plain_text = input()
            number_of_words= self.check_plain_text_length(plain_text)
            if number_of_words >= 5 and number_of_words <= 100:
                self.users["message"]= plain_text
                print(f'{number_of_words}/100 accepted length...')
            else:
                print(f'{number_of_words}/100 exceed limit FUCK YOU...')
                exit()
    
    def _verification_builder(self):
            print("Enter your message")
            # publicKey,R,s,message
            message = input()
            self.users["message"]= message
            print("Enter your Public Key.. ")
            publicKey = input()
            self.users["publicKey"]=self.check_bytes_info(publicKey).encode()
            print("Enter R then s: ")
            R = input()
            s = input()
            self.users["signature"]= [self.check_bytes_info(R).encode(),self.check_bytes_info(s).encode()]
            # else:
            #     print(f'wrong format FUCK YOU...')
            #     exit()

        
