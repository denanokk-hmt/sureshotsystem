#!/bin/bash -vx
#

########################################
#	POSTCODE.CGI 郵便番号から住所を検索
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
POSTCODE x7
FIN

check_attr_name $tmp-check $tmp-name > /dev/null
ERROR_CHECK

########################################
#郵便番号の取得
postcode=$(nameread POSTCODE $tmp-name)

#1.郵便番号 2.都道府県 3.市区町村 4.住所
cat /home/sureshotsystem/DATA/POSTCODES     |
awk '$1=="'$postcode'"'                     > $tmp-address


########################################
#画面表示
cat << FIN
Content-type: text/plain

FIN

echo ""
cat $tmp-address


########################################
#終了処理
rm -f $tmp-*
exit 0
