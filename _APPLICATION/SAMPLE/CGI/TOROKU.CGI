#!/bin/bash -vx
#

########################################
#	TOROKU.CGI name & Age
#
#	Written by hiramatsu

########################################
#
apld=/home/sureshotsystem/_APPLICATION/SAMPLE
exec 2> $apld/LOG/LOG.$(basename $0).$(date +%Y%m%d)
tmp=/tmp/SAMPLE/tmp_$$
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
FAMILYNAME x12
GIVENNAME x20
AGE N2
FIN

check_attr_name $tmp-check $tmp-name > $tmp-result || echo "NG" > $tmp-NG


########################################
#モード設定
mode=$(nameread MODE $tmp-name)
[ "$mode" == "" ] && mode="INIT"
[ "$mode" == "_" ] && mode="INIT"
[ "$(cat $tmp-NG)" == "NG" ] && mode="NG"


########################################
#モードよるHTML設定
case $mode in
INIT)
	message='下のフォームに入力してください。'
	cat $apld/HTML/TOROKU.HTML		|
	sed -e "s/###MESSAGE###/$message/"	> $tmp-html
	;;
NG)
	message='もう一度入力してください。'
	cat $apld/HTML/TOROKU.HTML		|
	sed -e "s/###MESSAGE###/$message/"	> $tmp-html
	;;
CHK)
	cat <<- FIN | LANG=C sort > $tmp-table
	FAMILYNAME 1 姓
	GIVENNAME 2 名
	AGE 3 年齢(年代)
	FIN

	cat $tmp-name								|
	nameread -el 'FAMILYNAME|GIVENNAME|AGE'	    |
	LNAG=C sort -k1,1							|
	loopj num=1 $tmp-table -					|
	LNAG=C sort -k2,2							> $tmp-records
	# 1:name 2:表示順 3:項目名 4:値

#	cat $apld/HTML/TOROKU.CHK.HTML				|
	mojihame -lRECORDS $apld/HTML/TOROKU.CHK.HTML $tmp-records             > $tmp-html
	;;
REG)
	cat $tmp-name                               |
	nameread -el 'FAMILYNAME|GIVENNAME|AGE'     |
    LANG=C sort -k1,1                           > $apld/INPUT/$(date +%Y%m%d).$(date +%H%M%S).$$
	echo "受け付けました。"						> $tmp-html
	;;
*)
	echo 未実装 $mode							> $tmp-html
	;;
esac


########################################
#画面表示
cat << FIN
Content-type: text/html

FIN

echo ""
cat $tmp-html


########################################
#終了処理
#rm -f $tmp-*
exit 0
