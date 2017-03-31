#!/bin/bash
#

##################################################
#       test.cgi
#
#       written by hmt 2016.2.20

##################################################
# 基本設定
LANG=ja_JP.UTF-8
PATH=/home/:/usr/local/bin:$PATH
apld=/home/sureshotsystem/APPLICATION/LOGIN
exec 2> /dev/null
exec 2> $apld/LOG/LOG.$(basename $0).$(date +%Y%m%d)
tmp=/tmp/tmp_$$

##################################################
# エラーチェック
ERROR_CHECK(){
	[ $(plus ${PIPESTATUS[@]}) -eq 0 ]  && return
cat <<- FIN
	Content-type: text/html
	NG Input
FIN
	cat $tmp-result
	exit 1
}

##################################################
# 変数の取得
if [ ! -z $CONTENT_LENGTH ]; then
	dd bs=$CONTENT_LENGTH |
	cgi-name -n_ -s_ > $tmp-name
	touch $tmp-test1
else
	touch $tmp-test2
	touch $tmp-name
fi

##################################################
# 変数のチェック
cat << FIN > $tmp-check
NAME x20
FIN

check_attr_name $tmp-check $tmp-name > $tmp-result || echo "NG" > $tmp-NG


##################################################
# 変数の読み出し
mode=$(nameread MODE $tmp-name)
[ "$mode" = "" ] && mode="INIT"
[ "$mode" = "_" ] && mode="INIT"
[ "$(cat $tmp-NG)" "NG" ] && mode="NG"

cat $mode > $tmp-mode
case $mode in
INIT)
	cat $mode > $tmp-init
	msg=下のフォームに入力してください。
	cat $apld/HTML/test.html	|
	sed -e "s;###MESSAGE###;$msg;"	> $tmp-html
	;;
NG)
	cat $mode > $tmp-modeng
	msg='もう一度入力してください。'
	cat $apld/HTML/test.html	|
	sed -e "s;###MESSAGE###;$msg;"	> $tmp-html
	;;
*)
	echo  未実装 $mode > $tmp-html
esac


##################################################
# 変数の読み出し
echo "Content-type: text/html"
echo ""
cat $tmp-html

#cat $tmp-name   |
#sed -e 's/$/<br>/g'

#rm -f $tmp-*
exit 0
