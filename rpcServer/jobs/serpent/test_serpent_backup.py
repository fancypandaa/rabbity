import sys
import getopt

import helper as help_functions
import serpent as normal_serpent
import observer as observer

def normal_serpent_encrypt(chunk_messages,user_key):
    cipher_message=""
    for plain_text in chunk_messages:
        plain_text = replace_space_with_zero(plain_text)
        plain_text=convert_string_to_binary(plain_text)
        cipher_message += normal_serpent.encrypt(plain_text, help_functions.convertToBitstring(user_key, 256))
    return cipher_message

def normal_serpent_decrypt(cipher_messages,user_key):
    plain_text=""
    for cipher_text in cipher_messages:
        plain_text += normal_serpent.decrypt(cipher_text, help_functions.convertToBitstring(user_key, 256))
    return plain_text

def main():
    observer_object = observer.Observer(["plainText", "userKey", "cipherText"])
    opts, args = getopt.getopt(sys.argv[1:], "edhbt:k:p:c:i:")

    if args:
        help_functions.helpExit("Sorry, can't make sense of this: '%s'" % args)

    options = {}
    for opt, arg in opts:
        if opt == "-t":
            observer_object.addTag(arg)
        else:
            if opt in options.keys():
                help_functions.helpExit("Multiple occurrences of " + opt)
            else:
                options[str.strip(opt)] = str.strip(arg)
    
    # Not more than one mode
    mode = None
    for key in options.keys():
        if key in ["-e", "-d", "-h"]:
            if mode:
                help_functions.helpExit("You can only specify one mode")
            else:
                mode = key

    if not mode:
        help_functions.helpExit("No mode specified")
   
    # Put plainText, userKey, cipherText in bitstring format.
    plain_text =  cipher_text = user_key = None
    
    if  ('-p') in str(options):
        plain_text = options["-p"]
        chunk_messages=help_functions.chunk_and_plain_text_128bit(plain_text)
        
    if ('-c') in str(options):
        cipher_text = options["-c"]
        
    if mode == "-e":
        if not plain_text:
            help_functions.helpExit("-p (plaintext) is required when doing -e (encrypt)")
    if mode == "-d":
        if not cipher_text:
            help_functions.helpExit("-c (ciphertext) is required when doing -d (decrypt)")
             
    if mode == "-e":
        if ('-k') in str(options):
            user_key = options['-k']
        else:
            user_key = help_functions.key_gen()
        print('************************** Starting encryption **************************')
        print('The Plain text is: ', plain_text)
        print("The Cipher text is: ",normal_serpent_encrypt(chunk_messages,user_key) )
        print("The key is: ", user_key)
    elif mode == "-d":
        user_key = options["-k"]
        if not user_key:
            help_functions.helpExit('-k (key) required with -d (decrypt)')
     
        print('************************** Starting decryption **************************')
        bits = help_functions.chunk_cipher_into_128bit(cipher_text)
        plain_text_bits = normal_serpent_decrypt(bits,user_key)
        plain_text = help_functions.convert_binary_to_string(plain_text_bits)
        plain_text = help_functions.replace_zeros_with_spaces(plain_text)
        print('The Cipher text is: ', cipher_text)
        # print('The Plain text is: ', normal_serpent.decrypt(cipher_text, help_functions.convertToBitstring(user_key, 256)))
        print('The original text ' ,plain_text)
    else:
        help_functions.helpExit()

if __name__ == "__main__":
    main()