#!/bin/bash

./nanopb-0.4.6/generator-bin/protoc -I=protobufs --python_out black_lager `ls protobufs/*.proto`

if [[ $OSTYPE == 'darwin'* ]]; then
  sed -i '' -E 's/^(import.*_pb2)/from . \1/' black_lager/*.py
  sed -i '' -E "s/^None = 0/globals()['None'] = 0/" black_lager/mesh_pb2.py
else
  sed -i -e 's/^import.*_pb2/from . \0/' black_lager/*.py
  sed -i -e "s/^None = 0/globals()['None'] = 0/" black_lager/mesh_pb2.py
fi
