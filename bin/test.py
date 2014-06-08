# encoding: utf-8
import zmq
import sys
import time
import uuid
import json

sys.path.append('..')
from core import RequestHandler

def handler(*args):
    print args

proto = RequestHandler(handler=handler)
proto.get_task()

# for request in range (1,10):
#     proto.store(request)
