#!/usr/bin/env python3
"""The Python implementation of the GRPC tick_eval.TickEval server."""

from concurrent import futures
import time
import logging

import grpc

import tick_eval_pb2
import tick_eval_pb2_grpc
import pdb

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


# Greeter->TickEval ("service")
# SayHello->EvalSingle ("rpc under service")
# GreeterServicer->TickEvalServicer ("generated in pb2_grpc")

class TickEval(tick_eval_pb2_grpc.TickEvalServicer):

    def EvalSingle(self, request, context):

        # pdb.set_trace()
        
        print(str(request.lastDT) + ';' + \
              str(request.lastOpen) + ';' + \
              str(request.lastHigh) + ';' + \
              str(request.lastLow) + ';' + \
              str(request.lastClose) + ';' + \
              str(request.lastVolume) + ';' + \
              str(request.posSize))
        message_back = "buyToCover"
        return tick_eval_pb2.OrderResponse(OrderType=message_back)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tick_eval_pb2_grpc.add_TickEvalServicer_to_server(TickEval(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
