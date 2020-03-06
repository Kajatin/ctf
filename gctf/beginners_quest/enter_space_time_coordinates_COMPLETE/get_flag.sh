#!/bin/bash

curl -s https://storage.googleapis.com/gctf-2019-attachments/00c2a73eec8abb4afb9c3ef3a161b64b451446910535bfc0cc81c2b04aa132ed --output attachment

mv attachment attachment.zip
unzip -qo attachment.zip

strings rand2 | grep CTF | rev | cut -d ' ' -f1 | rev
