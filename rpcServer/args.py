import argparse
from rpc_server import RpcServer
from queues import Queues
from celery import Celery

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
        print("nn")
    elif (queues.check_queue(args.queue)):
        server = RpcServer(args.queue)
    else:
        print("wrong queue name......")
