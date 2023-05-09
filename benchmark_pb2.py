# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: benchmark.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='benchmark.proto',
  package='benchmark',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x62\x65nchmark.proto\x12\tbenchmark\"%\n\x12GetProgramsRequest\x12\x0f\n\x07machine\x18\x01 \x01(\t\"\'\n\x13GetProgramsResponse\x12\x10\n\x08programs\x18\x01 \x03(\t\"Z\n\x13SetEpochTimeRequest\x12\x0f\n\x07machine\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x01(\t\x12\x10\n\x08\x65poch_id\x18\x03 \x01(\x03\x12\x0f\n\x07seconds\x18\x04 \x01(\x03\"\x16\n\x14SetEpochTimeResponse\"7\n\x13GetEpochTimeRequest\x12\x0f\n\x07machine\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x03(\t\"[\n\x14GetEpochTimeResponse\x12\x0f\n\x07machine\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x01(\t\x12\x10\n\x08\x65poch_id\x18\x03 \x01(\x03\x12\x0f\n\x07seconds\x18\x04 \x01(\x03\"7\n\x13\x44\x65lEpochTimeRequest\x12\x0f\n\x07machine\x18\x01 \x01(\t\x12\x0f\n\x07program\x18\x02 \x01(\t\"\x16\n\x14\x44\x65lEpochTimeResponse2\xdd\x02\n\x10\x42\x65nchmarkService\x12N\n\x0bGetPrograms\x12\x1d.benchmark.GetProgramsRequest\x1a\x1e.benchmark.GetProgramsResponse\"\x00\x12Q\n\x0cSetEpochTime\x12\x1e.benchmark.SetEpochTimeRequest\x1a\x1f.benchmark.SetEpochTimeResponse\"\x00\x12S\n\x0cGetEpochTime\x12\x1e.benchmark.GetEpochTimeRequest\x1a\x1f.benchmark.GetEpochTimeResponse\"\x00\x30\x01\x12Q\n\x0c\x44\x65lEpochTime\x12\x1e.benchmark.DelEpochTimeRequest\x1a\x1f.benchmark.DelEpochTimeResponse\"\x00\x62\x06proto3'
)




_GETPROGRAMSREQUEST = _descriptor.Descriptor(
  name='GetProgramsRequest',
  full_name='benchmark.GetProgramsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='benchmark.GetProgramsRequest.machine', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=67,
)


_GETPROGRAMSRESPONSE = _descriptor.Descriptor(
  name='GetProgramsResponse',
  full_name='benchmark.GetProgramsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='programs', full_name='benchmark.GetProgramsResponse.programs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=69,
  serialized_end=108,
)


_SETEPOCHTIMEREQUEST = _descriptor.Descriptor(
  name='SetEpochTimeRequest',
  full_name='benchmark.SetEpochTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='benchmark.SetEpochTimeRequest.machine', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='program', full_name='benchmark.SetEpochTimeRequest.program', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch_id', full_name='benchmark.SetEpochTimeRequest.epoch_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='benchmark.SetEpochTimeRequest.seconds', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=110,
  serialized_end=200,
)


_SETEPOCHTIMERESPONSE = _descriptor.Descriptor(
  name='SetEpochTimeResponse',
  full_name='benchmark.SetEpochTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=202,
  serialized_end=224,
)


_GETEPOCHTIMEREQUEST = _descriptor.Descriptor(
  name='GetEpochTimeRequest',
  full_name='benchmark.GetEpochTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='benchmark.GetEpochTimeRequest.machine', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='program', full_name='benchmark.GetEpochTimeRequest.program', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=226,
  serialized_end=281,
)


_GETEPOCHTIMERESPONSE = _descriptor.Descriptor(
  name='GetEpochTimeResponse',
  full_name='benchmark.GetEpochTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='benchmark.GetEpochTimeResponse.machine', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='program', full_name='benchmark.GetEpochTimeResponse.program', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epoch_id', full_name='benchmark.GetEpochTimeResponse.epoch_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='benchmark.GetEpochTimeResponse.seconds', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=283,
  serialized_end=374,
)


_DELEPOCHTIMEREQUEST = _descriptor.Descriptor(
  name='DelEpochTimeRequest',
  full_name='benchmark.DelEpochTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='machine', full_name='benchmark.DelEpochTimeRequest.machine', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='program', full_name='benchmark.DelEpochTimeRequest.program', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=376,
  serialized_end=431,
)


_DELEPOCHTIMERESPONSE = _descriptor.Descriptor(
  name='DelEpochTimeResponse',
  full_name='benchmark.DelEpochTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=433,
  serialized_end=455,
)

DESCRIPTOR.message_types_by_name['GetProgramsRequest'] = _GETPROGRAMSREQUEST
DESCRIPTOR.message_types_by_name['GetProgramsResponse'] = _GETPROGRAMSRESPONSE
DESCRIPTOR.message_types_by_name['SetEpochTimeRequest'] = _SETEPOCHTIMEREQUEST
DESCRIPTOR.message_types_by_name['SetEpochTimeResponse'] = _SETEPOCHTIMERESPONSE
DESCRIPTOR.message_types_by_name['GetEpochTimeRequest'] = _GETEPOCHTIMEREQUEST
DESCRIPTOR.message_types_by_name['GetEpochTimeResponse'] = _GETEPOCHTIMERESPONSE
DESCRIPTOR.message_types_by_name['DelEpochTimeRequest'] = _DELEPOCHTIMEREQUEST
DESCRIPTOR.message_types_by_name['DelEpochTimeResponse'] = _DELEPOCHTIMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProgramsRequest = _reflection.GeneratedProtocolMessageType('GetProgramsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROGRAMSREQUEST,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.GetProgramsRequest)
  })
_sym_db.RegisterMessage(GetProgramsRequest)

GetProgramsResponse = _reflection.GeneratedProtocolMessageType('GetProgramsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROGRAMSRESPONSE,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.GetProgramsResponse)
  })
_sym_db.RegisterMessage(GetProgramsResponse)

SetEpochTimeRequest = _reflection.GeneratedProtocolMessageType('SetEpochTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETEPOCHTIMEREQUEST,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.SetEpochTimeRequest)
  })
_sym_db.RegisterMessage(SetEpochTimeRequest)

SetEpochTimeResponse = _reflection.GeneratedProtocolMessageType('SetEpochTimeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETEPOCHTIMERESPONSE,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.SetEpochTimeResponse)
  })
_sym_db.RegisterMessage(SetEpochTimeResponse)

GetEpochTimeRequest = _reflection.GeneratedProtocolMessageType('GetEpochTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETEPOCHTIMEREQUEST,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.GetEpochTimeRequest)
  })
_sym_db.RegisterMessage(GetEpochTimeRequest)

GetEpochTimeResponse = _reflection.GeneratedProtocolMessageType('GetEpochTimeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETEPOCHTIMERESPONSE,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.GetEpochTimeResponse)
  })
_sym_db.RegisterMessage(GetEpochTimeResponse)

DelEpochTimeRequest = _reflection.GeneratedProtocolMessageType('DelEpochTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELEPOCHTIMEREQUEST,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.DelEpochTimeRequest)
  })
_sym_db.RegisterMessage(DelEpochTimeRequest)

DelEpochTimeResponse = _reflection.GeneratedProtocolMessageType('DelEpochTimeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELEPOCHTIMERESPONSE,
  '__module__' : 'benchmark_pb2'
  # @@protoc_insertion_point(class_scope:benchmark.DelEpochTimeResponse)
  })
_sym_db.RegisterMessage(DelEpochTimeResponse)



_BENCHMARKSERVICE = _descriptor.ServiceDescriptor(
  name='BenchmarkService',
  full_name='benchmark.BenchmarkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=458,
  serialized_end=807,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPrograms',
    full_name='benchmark.BenchmarkService.GetPrograms',
    index=0,
    containing_service=None,
    input_type=_GETPROGRAMSREQUEST,
    output_type=_GETPROGRAMSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetEpochTime',
    full_name='benchmark.BenchmarkService.SetEpochTime',
    index=1,
    containing_service=None,
    input_type=_SETEPOCHTIMEREQUEST,
    output_type=_SETEPOCHTIMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetEpochTime',
    full_name='benchmark.BenchmarkService.GetEpochTime',
    index=2,
    containing_service=None,
    input_type=_GETEPOCHTIMEREQUEST,
    output_type=_GETEPOCHTIMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DelEpochTime',
    full_name='benchmark.BenchmarkService.DelEpochTime',
    index=3,
    containing_service=None,
    input_type=_DELEPOCHTIMEREQUEST,
    output_type=_DELEPOCHTIMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BENCHMARKSERVICE)

DESCRIPTOR.services_by_name['BenchmarkService'] = _BENCHMARKSERVICE

# @@protoc_insertion_point(module_scope)
