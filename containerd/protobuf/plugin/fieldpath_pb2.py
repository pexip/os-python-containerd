# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: containerd/protobuf/plugin/fieldpath.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from containerd.vendor.google.protobuf import descriptor_pb2 as containerd_dot_vendor_dot_google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='containerd/protobuf/plugin/fieldpath.proto',
  package='containerd.plugin',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n*containerd/protobuf/plugin/fieldpath.proto\x12\x11\x63ontainerd.plugin\x1a\x32\x63ontainerd/vendor/google/protobuf/descriptor.proto:5\n\rfieldpath_all\x12\x1c.google.protobuf.FileOptions\x18\xc4\xee\x03 \x01(\x08:4\n\tfieldpath\x12\x1f.google.protobuf.MessageOptions\x18\x90\xf7\x03 \x01(\x08')
  ,
  dependencies=[containerd_dot_vendor_dot_google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


FIELDPATH_ALL_FIELD_NUMBER = 63300
fieldpath_all = _descriptor.FieldDescriptor(
  name='fieldpath_all', full_name='containerd.plugin.fieldpath_all', index=0,
  number=63300, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FIELDPATH_FIELD_NUMBER = 64400
fieldpath = _descriptor.FieldDescriptor(
  name='fieldpath', full_name='containerd.plugin.fieldpath', index=1,
  number=64400, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['fieldpath_all'] = fieldpath_all
DESCRIPTOR.extensions_by_name['fieldpath'] = fieldpath
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

containerd_dot_vendor_dot_google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(fieldpath_all)
containerd_dot_vendor_dot_google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(fieldpath)

# @@protoc_insertion_point(module_scope)
