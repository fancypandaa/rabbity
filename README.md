# Rabbity (DEMO VERSION)


Rabbity is a collection of modern cryptography algorithms of complex algorithms and unpopular techniques.


![--rabbity header](https://github.com/fancypandaa/rabbity/blob/intro/rabbity.png)

Introduction
-----------
Rabbity depends on a decentralized and multi-tasking client-server pattern.
Work by RPC technology using Rabbitmq.

Architecture
-----------
![](https://github.com/fancypandaa/rabbity/blob/intro/Untitled%20Diagram.drawio.png)

rabbity approach is a decouple structure, which means you can run any algorithm individually,
the design depends on every client representing only one crypto algorithm you choose it from the beginning,
if you need to change, you must run a new client instance.

How to use it
-------
 First unload the tool.
```
git clone https://github.com/fancypandaa/rabbity.git
cd rabbity

chmod u+x rabbity.sh
./rabbity.sh
```
If you face some problems installing the tool, it is probably due to Python versions conflicts, you should run a Python 2.7 environment
```
source env/bin/activate
pip3 install -r requirements.txt
<!-- server -->
python3 rpcServer/args.py -q 'serpent' 
<!-- client -->
python3 rpcClient/args.py -o 'serpent'
```

**HELP  AND OPTIONS**
```
user:~$ python3 rabbity.py --help
usage: python3 rabbity.py -q <> -o <> [-h] [-v] 

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -q, --queue           create server instace with queue job (ex:serpent,...etc)
                        
  -o, --option          choose algoritm you want (ex: serpent,galaxy,...etc)
```


Disclaimer
-------
This tool has been published educational purposes. It is intended to help people how to use complex cryptography and unpopular strong algorithm who to use in very simple way.

Reference
-------
This all the reference we depend on it.
https://en.wikipedia.org/wiki/Cryptography#Symmetric-key_cryptography
https://www.cl.cam.ac.uk/~rja14/serpent.html
https://www.researchgate.net/figure/Serpent-Encryption-Algorithm_fig2_313899040
https://www.simplilearn.com/tutorials/cryptography-tutorial/aes-encryption 

Happy hacking!
-------


## License

The content of this project itself is licensed under the [Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US), and the underlying source code used to format and display that content is licensed under the [MIT license](http://opensource.org/licenses/mit-license.php).

Copyright, 2023 by [JOE]

-------------
