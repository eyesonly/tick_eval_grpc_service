#!/usr/bin/env python3
"""The Python implementation of the GRPC tick_eval.TickEval client."""


from __future__ import print_function
import logging

import grpc

import tick_eval_pb2
import tick_eval_pb2_grpc
import sys
import pandas as pd
import datetime
import pytz

EXCEL_DATE_SYSTEM_PC=datetime.datetime(1900, 1, 1, 0, 0, 0).replace(tzinfo=pytz.UTC)
import pdb

filenamen = str(sys.argv[1])
df = pd.DataFrame()
df  = pd.read_csv(filenamen, index_col='timestamp', parse_dates=True,
                       names=['timestamp', 'open', 'high', 'low', 'close', 'vol', 'vwap', 'entry_price', 'open_pnl', 'pos_size'],
                       dtype=float, header=0)
df = df.applymap(lambda x: round(x, 3))
reverse_parser = lambda x: round((( (x - EXCEL_DATE_SYSTEM_PC).days + (x - EXCEL_DATE_SYSTEM_PC).seconds / 86400 ) + 2), 6)
df['ind'] = df.index
df['excelDT'] = df.ind.apply(reverse_parser)

# df2 = pd.DataFrame()
# df2 = df
# del df2['ind']
# del df2['entry_price']
# del df2['open_pnl']
# del df2['excelDT']
# del df2['pos_size']
# rnd = pd.DataFrame()
# rnd = df2.applymap(lambda x: round(x, 3))
# filenamen = '/home/jonathan/bitmex/SI_testcase_backtest.csv'
# rnd.to_csv(filenamen)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    # with grpc.insecure_channel('10.12.78.137:50051') as channel:
    pos = 0
    entry_price = 0
    open_pnl = 0
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = tick_eval_pb2_grpc.TickEvalStub(channel)
        for index, row in df.iterrows():
            
            entry_price = row.entry_price
            open_pnl = row.open_pnl
            pos = int(row.pos_size)
                
            barpos = tick_eval_pb2.BarPos(lastDT=row.excelDT, \
                                      lastOpen=row.open, \
                                      lastHigh=row.high, \
                                      lastLow=row.low, \
                                      lastClose=row.close,\
                                      lastVolume=row.vol, \
                                      posSize=pos, \
                                          entryPrice = entry_price, \
                                          openPnL = open_pnl)                                          
            lastOpen = row.open
            response = stub.EvalSingle(barpos)
            # print(str(row.excelDT) + "; Order type client received: " + response.OrderType)
            if response.OrderType != "":
                print(row.excelDT, " " , response.OrderType)
                # if response.OrderType == "open_long":
                #     # pos = 1
                # if response.OrderType == "close_long":
                #     # pos = 0
                #     # entry_price = 0
                # if response.OrderType == "open_short":
                #     pos = -1
                # if response.OrderType == "close_short":
                #     pos = 0
                #     # entry_price = 0
                # if response.OrderType == "reverse_long":
                #     pos = -1
                #     # entry_price = 0
                # if response.OrderType == "reverse_short":
                #     pos = 1
                #     # entry_price = 0


if __name__ == '__main__':
    logging.basicConfig()
    run()
