#!/usr/bin/env python3
"""The Python implementation of the GRPC tick_eval.TickEval client."""

from __future__ import print_function
import logging

import grpc

import tick_eval_pb2
import tick_eval_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # with grpc.insecure_channel('10.12.78.137:50051') as channel:
    with grpc.insecure_channel('192.168.1.231:50051') as channel:
        stub = tick_eval_pb2_grpc.TickEvalStub(channel)
        barpos = tick_eval_pb2.BarPos(lastDT=43123.000000, \
                                      lastOpen=51, \
                                      lastHigh=52, \
                                      lastLow=51, \
                                      lastClose=51.5,\
                                      lastVolume=777, \
                                      posSize=-1)
        response = stub.EvalSingle(barpos)
        # response = stub.EvalSingle(tick_eval_pb2.BarPos(lastDT=21.123456, lastOpen=51))
        print("Order type client received: " + response.OrderType)
        # response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='Second'))
        # print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
