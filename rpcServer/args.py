import argparse
from rpc_server import RpcServer
from queues import Queues
# from celery import Celery
import multiprocessing 

def serpentWorker():
    RpcServer("serpent")
    
def ecdsaWorker():
    RpcServer("ecdsa")

def mulitProcessing():
    p1 = multiprocessing.Process(target=serpentWorker) 
    p2 = multiprocessing.Process(target=ecdsaWorker) 
    # starting processes 
    p1.start() 
    p2.start() 
    # process IDs 
    print("ID of process p1: {}".format(p1.pid)) 
    print("ID of process p2: {}".format(p2.pid)) 
    p1.join() 
    p2.join() 
        # both processes finished 
    print("Both processes finished execution!")   
    # check if processes are alive 
    print("Process p1 is alive: {}".format(p1.is_alive())) 
    print("Process p2 is alive: {}".format(p2.is_alive())) 
    


parser = argparse.ArgumentParser(description='RPC Rabbity Server')
parser.add_argument('--queue','-q',type=str)
parser.add_argument('--details', '-d',type=str)
parser.add_argument('--helps', '-H',type=None)

args = parser.parse_args()
queues = Queues()

if args.details and args.queue:
    print("Wrongs Input select only one argument")
    print("for more helps -h or --help")
elif args.details:
    queues.display_queue_info()
elif args.helps:
    print("under works")
elif args.queue:
    if args.queue == '*':
        mulitProcessing()
    elif (queues.check_queue(args.queue)):
        server = RpcServer(args.queue)
    else:
        print("wrong queue name......")
