#!/bin/bash -vx
#

########################################
#	AJAX.CGI name & Age
#
#	Written by hiramatsu

########################################
#
apld=/home/sureshotsystem/APPLICATION/SAMPLE
exec 2> $apld/LOG/LOG.$(basename $0).$(date +%Y%m%d)
tmp=/tmp/tmp_$$
LANG=ja_JP.UTF-8
PATH=/home/:/home/UTL:/home/TOOL/open-usp-tukubai-2014061402/COMMANDS:$PATH

echo "Content-type: text/plain"
sleep 3
echo ""
date "+%Y%m%d %H%M%S"

exit 0
