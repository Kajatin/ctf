#!/bin/bash

curl -s https://storage.googleapis.com/gctf-2019-attachments/4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a --output attachment

mv attachment{,.zip}
unzip -qo attachment.zip
