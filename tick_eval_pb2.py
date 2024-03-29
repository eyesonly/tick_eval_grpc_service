# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tick_eval.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tick_eval.proto',
  package='tickeval',
  syntax='proto3',
  serialized_options=_b('\n\031io.grpc.examples.tickevalB\rTickEvalProtoP\001\242\002\003TEV'),
  serialized_pb=_b('\n\x0ftick_eval.proto\x12\x08tickeval\"\xbe\x01\n\x06\x42\x61rPos\x12\x0e\n\x06lastDT\x18\x01 \x01(\x01\x12\x10\n\x08lastOpen\x18\x02 \x01(\x01\x12\x10\n\x08lastHigh\x18\x03 \x01(\x01\x12\x0f\n\x07lastLow\x18\x04 \x01(\x01\x12\x11\n\tlastClose\x18\x05 \x01(\x01\x12\x12\n\nlastVolume\x18\x06 \x01(\x01\x12\x0f\n\x07posSize\x18\x07 \x01(\x11\x12\x12\n\nentryPrice\x18\x08 \x01(\x01\x12\x0f\n\x07openPnL\x18\t \x01(\x01\x12\x12\n\nextraField\x18\n \x01(\t\"\x19\n\tServerDet\x12\x0c\n\x04port\x18\x01 \x01(\t\"\"\n\rOrderResponse\x12\x11\n\tOrderType\x18\x01 \x01(\t\"$\n\x0cStopResponse\x12\x14\n\x0cresponseBack\x18\x01 \x01(\t2\x82\x01\n\x08TickEval\x12\x39\n\nEvalSingle\x12\x10.tickeval.BarPos\x1a\x17.tickeval.OrderResponse\"\x00\x12;\n\nStopServer\x12\x13.tickeval.ServerDet\x1a\x16.tickeval.StopResponse\"\x00\x42\x32\n\x19io.grpc.examples.tickevalB\rTickEvalProtoP\x01\xa2\x02\x03TEVb\x06proto3')
)




_BARPOS = _descriptor.Descriptor(
  name='BarPos',
  full_name='tickeval.BarPos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lastDT', full_name='tickeval.BarPos.lastDT', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastOpen', full_name='tickeval.BarPos.lastOpen', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastHigh', full_name='tickeval.BarPos.lastHigh', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastLow', full_name='tickeval.BarPos.lastLow', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastClose', full_name='tickeval.BarPos.lastClose', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastVolume', full_name='tickeval.BarPos.lastVolume', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='posSize', full_name='tickeval.BarPos.posSize', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entryPrice', full_name='tickeval.BarPos.entryPrice', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='openPnL', full_name='tickeval.BarPos.openPnL', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraField', full_name='tickeval.BarPos.extraField', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=220,
)


_SERVERDET = _descriptor.Descriptor(
  name='ServerDet',
  full_name='tickeval.ServerDet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='tickeval.ServerDet.port', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=247,
)


_ORDERRESPONSE = _descriptor.Descriptor(
  name='OrderResponse',
  full_name='tickeval.OrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='OrderType', full_name='tickeval.OrderResponse.OrderType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=283,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='tickeval.StopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responseBack', full_name='tickeval.StopResponse.responseBack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=321,
)

DESCRIPTOR.message_types_by_name['BarPos'] = _BARPOS
DESCRIPTOR.message_types_by_name['ServerDet'] = _SERVERDET
DESCRIPTOR.message_types_by_name['OrderResponse'] = _ORDERRESPONSE
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BarPos = _reflection.GeneratedProtocolMessageType('BarPos', (_message.Message,), dict(
  DESCRIPTOR = _BARPOS,
  __module__ = 'tick_eval_pb2'
  # @@protoc_insertion_point(class_scope:tickeval.BarPos)
  ))
_sym_db.RegisterMessage(BarPos)

ServerDet = _reflection.GeneratedProtocolMessageType('ServerDet', (_message.Message,), dict(
  DESCRIPTOR = _SERVERDET,
  __module__ = 'tick_eval_pb2'
  # @@protoc_insertion_point(class_scope:tickeval.ServerDet)
  ))
_sym_db.RegisterMessage(ServerDet)

OrderResponse = _reflection.GeneratedProtocolMessageType('OrderResponse', (_message.Message,), dict(
  DESCRIPTOR = _ORDERRESPONSE,
  __module__ = 'tick_eval_pb2'
  # @@protoc_insertion_point(class_scope:tickeval.OrderResponse)
  ))
_sym_db.RegisterMessage(OrderResponse)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), dict(
  DESCRIPTOR = _STOPRESPONSE,
  __module__ = 'tick_eval_pb2'
  # @@protoc_insertion_point(class_scope:tickeval.StopResponse)
  ))
_sym_db.RegisterMessage(StopResponse)


DESCRIPTOR._options = None

_TICKEVAL = _descriptor.ServiceDescriptor(
  name='TickEval',
  full_name='tickeval.TickEval',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=324,
  serialized_end=454,
  methods=[
  _descriptor.MethodDescriptor(
    name='EvalSingle',
    full_name='tickeval.TickEval.EvalSingle',
    index=0,
    containing_service=None,
    input_type=_BARPOS,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopServer',
    full_name='tickeval.TickEval.StopServer',
    index=1,
    containing_service=None,
    input_type=_SERVERDET,
    output_type=_STOPRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TICKEVAL)

DESCRIPTOR.services_by_name['TickEval'] = _TICKEVAL

# @@protoc_insertion_point(module_scope)
