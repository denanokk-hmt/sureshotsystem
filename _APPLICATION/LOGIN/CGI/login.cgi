#!/bin/bash

dd bs=$CONTENT_LENGTH > /tmp/hoge

echo "Content-type: text/html"
echo ""
echo "LOGIN!!"
