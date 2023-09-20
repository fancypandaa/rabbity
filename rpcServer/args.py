import argparse
from rpc_server import RpcServer
from queues import Queues


parser = argparse.ArgumentParser(description='RPC Rabbity Server')
parser.add_argument('--queue','-q',type=str)
parser.add_argument('--details', '-d',type=str)
args = parser.parse_args()
queues = Queues()

if args.details:
    if args.details == '*':
        queues.display_queue_info()

if args.queue:
    if (queues.check_queue(args.queue)):
        server = RpcServer(args.queue)
    else:
        print("wrong queue name......")
