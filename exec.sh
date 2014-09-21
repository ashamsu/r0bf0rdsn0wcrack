#!/bin/bash
cd /r0bf0rdsn0wcrack/
offset1 = ./getkbagloc.py
offset2 = ./getaesloc.py
echo "got dem offsets"
./iBootPayload offset1 offset2