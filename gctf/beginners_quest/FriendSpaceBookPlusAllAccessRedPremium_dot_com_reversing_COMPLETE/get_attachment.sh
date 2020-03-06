#!/bin/bash

curl -s https://storage.googleapis.com/gctf-2019-attachments/775e97ff94e7dfe79293b62abed7e1ad17cdc6ebc82c4873cdca201c40569624 --output attachment

mv attachment attachment.zip
unzip -qo attachment.zip
