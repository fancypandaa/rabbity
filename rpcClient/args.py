import argparse
from rpc_client import RpcClient


parser = argparse.ArgumentParser(description='RPC Rabbity client')
parser.add_argument('--option','-o',type=str)
args = parser.parse_args()

if args.option:
    default_queues=["galaxy","serpent","sheep","spider","zero"]
    if args.option in default_queues:
        server = RpcClient(args.option)
    else:
        print("wrong option name......")
