#!/bin/bash -vx
#

########################################
#	SELECT.ADDR.ADDR.CGI 住所一覧のプルダウン表示
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
#エラーチェック
ERROR_CHECK(){
	[ $(plus ${PIPESTATUS[@]}) -eq 0 ] && return
cat <<- FIN
	Context-type: text/html
	NG input
FIN
	cat $tmp-result
	exit 1
}


########################################
#POSTパラメーターの取得
if [ ! -z $CONTENT_LENGTH ]; then
	dd bs=$CONTENT_LENGTH |
	cgi-name -d_ -i_	> $tmp-name
else
	touch $tmp-name
fi


########################################
#バリデーション
cat << FIN > $tmp-check
PREF x8
CITY x40
FIN

check_attr_name $tmp-check $tmp-name > /dev/null
ERROR_CHECK


########################################
#PREFを取得
pref=$(nameread PREF $tmp-name)
city=$(nameread CITY $tmp-name)


########################################
#画面表示
cat << FIN > $tmp-html
<select id="ADDR">
    <option value="選択">--選択してください--</option>
RECORDS
    <option value="%1">%1</option>
RECORDS
</select>
FIN

echo "Content-Type: text/plain"
echo ""
awk '$2=="'$pref'"{print $3,$4}' /home/sureshotsystem/DATA/POSTCODES    |
awk '$1=="'$city'"{print $2}'                                           |
mojihame -d -lRECORDS $tmp-html -


########################################
#終了処理
rm -f $tmp-*
exit 0
