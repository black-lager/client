#!/bin/bash

./nanopb-0.4.6/generator-bin/protoc -I=protobufs --python_out mesh `ls protobufs/*.proto`

if [[ $OSTYPE == 'darwin'* ]]; then
  sed -i '' -E 's/^(import.*_pb2)/from . \1/' mesh/*.py
  sed -i '' -E "s/^None = 0/globals()['None'] = 0/" mesh/mesh_pb2.py
else
  sed -i -e 's/^import.*_pb2/from . \0/' mesh/*.py
  sed -i -e "s/^None = 0/globals()['None'] = 0/" mesh/mesh_pb2.py
fi
