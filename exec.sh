#!/bin/bash
cd /r0bf0rdsn0wcrack/
offset1 = python getkbagloc.py
offset2 = python getaesloc.py
echo "got dem offsets"
./iBootPayload offset1 offset2