#!/bin/bash

curl -s https://storage.googleapis.com/gctf-2019-attachments/768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf --output attachment

mv attachment attachment.zip
unzip -qo attachment.zip

chmod +x init_sat
