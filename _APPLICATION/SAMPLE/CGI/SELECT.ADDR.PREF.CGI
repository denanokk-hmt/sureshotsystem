#!/bin/bash -vx
#

########################################
#	SELECT.ADDR.PREF.CGI 都道府県一覧のプルダウン表示
#
#	Written by hiramatsu

########################################
#
apld=/home/sureshotsystem/APPLICATION/SAMPLE
exec 2> $apld/LOG/LOG.$(basename $0).$(date +%Y%m%d)
tmp=/tmp/tmp_$$
LANG=ja_JP.UTF-8
PATH=/home/:/home/UTL:/home/TOOL/open-usp-tukubai-2014061402/COMMANDS:$PATH


########################################
#画面表示
cat << FIN > $tmp-html
<select id="PREF" onchange="getCitySelect(this.value)">
    <option value="選択">--選択してください--</option>
RECORDS
    <option value="%1">%1</option>
RECORDS
</select>
FIN

echo "Content-Type: text/plain"
echo ""
mojihame -d -lRECORDS $tmp-html /home/sureshotsystem/DATA/PREF


########################################
#終了処理
rm -f $tmp-*
exit 0
