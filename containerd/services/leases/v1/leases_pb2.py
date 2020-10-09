# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/services/leases/v1/leases.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.gogoproto import gogo_pb2 as containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2
from containerd.vendor.google.protobuf import empty_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2
from containerd.vendor.google.protobuf import timestamp_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/services/leases/v1/leases.proto',
  package='containerd.services.leases.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/containerd/containerd/api/services/leases/v1;leases'),
  serialized_pb=_b('\n*containerd/services/leases/v1/leases.proto\x12\x1d\x63ontainerd.services.leases.v1\x1a&containerd/vendor/gogoproto/gogo.proto\x1a-containerd/vendor/google/protobuf/empty.proto\x1a\x31\x63ontainerd/vendor/google/protobuf/timestamp.proto\"\xbe\x01\n\x05Lease\x12\n\n\x02id\x18\x01 \x01(\t\x12\x38\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\x90\xdf\x1f\x01\xc8\xde\x1f\x00\x12@\n\x06labels\x18\x03 \x03(\x0b\x32\x30.containerd.services.leases.v1.Lease.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x94\x01\n\rCreateRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12H\n\x06labels\x18\x03 \x03(\x0b\x32\x38.containerd.services.leases.v1.CreateRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"E\n\x0e\x43reateResponse\x12\x33\n\x05lease\x18\x01 \x01(\x0b\x32$.containerd.services.leases.v1.Lease\")\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04sync\x18\x02 \x01(\x08\"\x1e\n\x0bListRequest\x12\x0f\n\x07\x66ilters\x18\x01 \x03(\t\"D\n\x0cListResponse\x12\x34\n\x06leases\x18\x01 \x03(\x0b\x32$.containerd.services.leases.v1.Lease\"$\n\x08Resource\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"a\n\x12\x41\x64\x64ResourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x08resource\x18\x02 \x01(\x0b\x32\'.containerd.services.leases.v1.ResourceB\x04\xc8\xde\x1f\x00\"d\n\x15\x44\x65leteResourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x08resource\x18\x02 \x01(\x0b\x32\'.containerd.services.leases.v1.ResourceB\x04\xc8\xde\x1f\x00\"\"\n\x14ListResourcesRequest\x12\n\n\x02id\x18\x01 \x01(\t\"Y\n\x15ListResourcesResponse\x12@\n\tresources\x18\x01 \x03(\x0b\x32\'.containerd.services.leases.v1.ResourceB\x04\xc8\xde\x1f\x00\x32\xd6\x04\n\x06Leases\x12\x65\n\x06\x43reate\x12,.containerd.services.leases.v1.CreateRequest\x1a-.containerd.services.leases.v1.CreateResponse\x12N\n\x06\x44\x65lete\x12,.containerd.services.leases.v1.DeleteRequest\x1a\x16.google.protobuf.Empty\x12_\n\x04List\x12*.containerd.services.leases.v1.ListRequest\x1a+.containerd.services.leases.v1.ListResponse\x12X\n\x0b\x41\x64\x64Resource\x12\x31.containerd.services.leases.v1.AddResourceRequest\x1a\x16.google.protobuf.Empty\x12^\n\x0e\x44\x65leteResource\x12\x34.containerd.services.leases.v1.DeleteResourceRequest\x1a\x16.google.protobuf.Empty\x12z\n\rListResources\x12\x33.containerd.services.leases.v1.ListResourcesRequest\x1a\x34.containerd.services.leases.v1.ListResourcesResponseB@Z>github.com/containerd/containerd/api/services/leases/v1;leasesX\x00\x62\x06proto3')
  ,
  dependencies=[containerd_dot_vendor_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LEASE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.leases.v1.Lease.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.leases.v1.Lease.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.leases.v1.Lease.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=406,
)

_LEASE = _descriptor.Descriptor(
  name='Lease',
  full_name='containerd.services.leases.v1.Lease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.Lease.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='containerd.services.leases.v1.Lease.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\337\037\001\310\336\037\000'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.leases.v1.Lease.labels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LEASE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=406,
)


_CREATEREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='containerd.services.leases.v1.CreateRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='containerd.services.leases.v1.CreateRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='containerd.services.leases.v1.CreateRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=406,
)

_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='containerd.services.leases.v1.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.CreateRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='containerd.services.leases.v1.CreateRequest.labels', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=557,
)


_CREATERESPONSE = _descriptor.Descriptor(
  name='CreateResponse',
  full_name='containerd.services.leases.v1.CreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lease', full_name='containerd.services.leases.v1.CreateResponse.lease', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=559,
  serialized_end=628,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='containerd.services.leases.v1.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.DeleteRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync', full_name='containerd.services.leases.v1.DeleteRequest.sync', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=630,
  serialized_end=671,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='containerd.services.leases.v1.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filters', full_name='containerd.services.leases.v1.ListRequest.filters', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=673,
  serialized_end=703,
)


_LISTRESPONSE = _descriptor.Descriptor(
  name='ListResponse',
  full_name='containerd.services.leases.v1.ListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='leases', full_name='containerd.services.leases.v1.ListResponse.leases', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=705,
  serialized_end=773,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='containerd.services.leases.v1.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.Resource.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='containerd.services.leases.v1.Resource.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=775,
  serialized_end=811,
)


_ADDRESOURCEREQUEST = _descriptor.Descriptor(
  name='AddResourceRequest',
  full_name='containerd.services.leases.v1.AddResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.AddResourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='containerd.services.leases.v1.AddResourceRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=813,
  serialized_end=910,
)


_DELETERESOURCEREQUEST = _descriptor.Descriptor(
  name='DeleteResourceRequest',
  full_name='containerd.services.leases.v1.DeleteResourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.DeleteResourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='containerd.services.leases.v1.DeleteResourceRequest.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=912,
  serialized_end=1012,
)


_LISTRESOURCESREQUEST = _descriptor.Descriptor(
  name='ListResourcesRequest',
  full_name='containerd.services.leases.v1.ListResourcesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='containerd.services.leases.v1.ListResourcesRequest.id', index=0,
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
  serialized_start=1014,
  serialized_end=1048,
)


_LISTRESOURCESRESPONSE = _descriptor.Descriptor(
  name='ListResourcesResponse',
  full_name='containerd.services.leases.v1.ListResourcesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='containerd.services.leases.v1.ListResourcesResponse.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\310\336\037\000'), file=DESCRIPTOR),
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
  serialized_start=1050,
  serialized_end=1139,
)

_LEASE_LABELSENTRY.containing_type = _LEASE
_LEASE.fields_by_name['created_at'].message_type = containerd_dot_vendor_dot_google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LEASE.fields_by_name['labels'].message_type = _LEASE_LABELSENTRY
_CREATEREQUEST_LABELSENTRY.containing_type = _CREATEREQUEST
_CREATEREQUEST.fields_by_name['labels'].message_type = _CREATEREQUEST_LABELSENTRY
_CREATERESPONSE.fields_by_name['lease'].message_type = _LEASE
_LISTRESPONSE.fields_by_name['leases'].message_type = _LEASE
_ADDRESOURCEREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_DELETERESOURCEREQUEST.fields_by_name['resource'].message_type = _RESOURCE
_LISTRESOURCESRESPONSE.fields_by_name['resources'].message_type = _RESOURCE
DESCRIPTOR.message_types_by_name['Lease'] = _LEASE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreateResponse'] = _CREATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['ListResponse'] = _LISTRESPONSE
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['AddResourceRequest'] = _ADDRESOURCEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResourceRequest'] = _DELETERESOURCEREQUEST
DESCRIPTOR.message_types_by_name['ListResourcesRequest'] = _LISTRESOURCESREQUEST
DESCRIPTOR.message_types_by_name['ListResourcesResponse'] = _LISTRESOURCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lease = _reflection.GeneratedProtocolMessageType('Lease', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LEASE_LABELSENTRY,
    '__module__' : 'containerd.services.leases.v1.leases_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.Lease.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LEASE,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.Lease)
  })
_sym_db.RegisterMessage(Lease)
_sym_db.RegisterMessage(Lease.LabelsEntry)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEREQUEST_LABELSENTRY,
    '__module__' : 'containerd.services.leases.v1.leases_pb2'
    # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.CreateRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)
_sym_db.RegisterMessage(CreateRequest.LabelsEntry)

CreateResponse = _reflection.GeneratedProtocolMessageType('CreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSE,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.CreateResponse)
  })
_sym_db.RegisterMessage(CreateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

ListResponse = _reflection.GeneratedProtocolMessageType('ListResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSE,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.ListResponse)
  })
_sym_db.RegisterMessage(ListResponse)

Resource = _reflection.GeneratedProtocolMessageType('Resource', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCE,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.Resource)
  })
_sym_db.RegisterMessage(Resource)

AddResourceRequest = _reflection.GeneratedProtocolMessageType('AddResourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESOURCEREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.AddResourceRequest)
  })
_sym_db.RegisterMessage(AddResourceRequest)

DeleteResourceRequest = _reflection.GeneratedProtocolMessageType('DeleteResourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESOURCEREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.DeleteResourceRequest)
  })
_sym_db.RegisterMessage(DeleteResourceRequest)

ListResourcesRequest = _reflection.GeneratedProtocolMessageType('ListResourcesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCESREQUEST,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.ListResourcesRequest)
  })
_sym_db.RegisterMessage(ListResourcesRequest)

ListResourcesResponse = _reflection.GeneratedProtocolMessageType('ListResourcesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESOURCESRESPONSE,
  '__module__' : 'containerd.services.leases.v1.leases_pb2'
  # @@protoc_insertion_point(class_scope:containerd.services.leases.v1.ListResourcesResponse)
  })
_sym_db.RegisterMessage(ListResourcesResponse)


DESCRIPTOR._options = None
_LEASE_LABELSENTRY._options = None
_LEASE.fields_by_name['created_at']._options = None
_CREATEREQUEST_LABELSENTRY._options = None
_ADDRESOURCEREQUEST.fields_by_name['resource']._options = None
_DELETERESOURCEREQUEST.fields_by_name['resource']._options = None
_LISTRESOURCESRESPONSE.fields_by_name['resources']._options = None

_LEASES = _descriptor.ServiceDescriptor(
  name='Leases',
  full_name='containerd.services.leases.v1.Leases',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1142,
  serialized_end=1740,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='containerd.services.leases.v1.Leases.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='containerd.services.leases.v1.Leases.Delete',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='containerd.services.leases.v1.Leases.List',
    index=2,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddResource',
    full_name='containerd.services.leases.v1.Leases.AddResource',
    index=3,
    containing_service=None,
    input_type=_ADDRESOURCEREQUEST,
    output_type=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteResource',
    full_name='containerd.services.leases.v1.Leases.DeleteResource',
    index=4,
    containing_service=None,
    input_type=_DELETERESOURCEREQUEST,
    output_type=containerd_dot_vendor_dot_google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListResources',
    full_name='containerd.services.leases.v1.Leases.ListResources',
    index=5,
    containing_service=None,
    input_type=_LISTRESOURCESREQUEST,
    output_type=_LISTRESOURCESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEASES)

DESCRIPTOR.services_by_name['Leases'] = _LEASES

# @@protoc_insertion_point(module_scope)
