#!/bin/bash -evx

SYSD=$(cd $(dirname $0) && pwd | awk '{print substr($0, 0, index($0, "sureshotsystem")+13)}')
exec 2> ${SYSD}/LOG/LOG.$(basename $0).$(date +%Y%m%d).$(date +%H%M%S).$$
tmp=/tmp/tmp_$$
LANG=ja_JP.UTF-8
PATH=/home/:/home/UTL:/usr/local/bin:${SYSD}/CGI/BIN:${SYSD}/INSTALL/open-usp-tukubai-2014061402/COMMANDS:$PATH

#ソース管理しないディレクトリ
mkdir ${SYSD}/DATA/BACKUP
mkdir ${SYSD}/DATA
mkdir ${SYSD}/DATA/NUMBERS
mkdir ${SYSD}/DATA/ORG_LV1-3
mkdir ${SYSD}/DATA/ORG_LV1-3/LV1
mkdir ${SYSD}/DATA/ORG_LV1-3/LV2
mkdir ${SYSD}/DATA/ORG_LV1-3/LV3
mkdir ${SYSD}/DATA/STUFF
mkdir ${SYSD}/DATA/STUFF/LOGIN
mkdir ${SYSD}/DATA/STUFF/LOGIN/LV1
mkdir ${SYSD}/DATA/STUFF/LOGIN/LV2
mkdir ${SYSD}/DATA/STUFF/LOGIN/LV3
mkdir ${SYSD}/DATA/STUFF/USERS
mkdir ${SYSD}/DATA/STUFF/USERS/LV1
mkdir ${SYSD}/DATA/STUFF/USERS/LV2
mkdir ${SYSD}/DATA/STUFF/USERS/LV3
mkdir ${SYSD}/IMG
mkdir ${SYSD}/LOCK
mkdir ${SYSD}/LOG
mkdir ${SYSD}/RCV
mkdir ${SYSD}/SAMPLE
mkdir ${SYSD}/SESSION
mkdir ${SYSD}/SND
mkdir ${SYSD}/TMP

#作成したディレクトリの権限変更
chmod -R 770 ${SYSD}/BACKUP/
chmod -R 770 ${SYSD}/IMG/
chmod -R 770 ${SYSD}/LOCK/
chmod -R 770 ${SYSD}/LOG/
chmod -R 770 ${SYSD}/RCV/
chmod -R 770 ${SYSD}/SAMPLE/
chmod -R 770 ${SYSD}/SESSION/
chmod -R 770 ${SYSD}/SND/
chmod -R 770 ${SYSD}/TMP/

#初期スタッフ登録
cp ./initial_stuff_login ${SYSD}/DATA/STUFF/LOGIN/LV1/1_login_20170101010101 
cp ./initial_stuff_login ${SYSD}/DATA/STUFF/LOGIN/LV2/1_login_20170101010101 
cp ./initial_stuff_login ${SYSD}/DATA/STUFF/LOGIN/LV3/1_login_20170101010101 
cp ./initial_stuff_users ${SYSD}/DATA/STUFF/USERS/LV1/1_stuff_20170101010101
cp ./initial_stuff_users ${SYSD}/DATA/STUFF/USERS/LV2/1_stuff_20170101010101
cp ./initial_stuff_users ${SYSD}/DATA/STUFF/USERS/LV3/1_stuff_20170101010101

#スタッフの初期採番
mkdir ${SYSD}/DATA/NUMBERS/STUFF
mkdir ${SYSD}/DATA/NUMBERS/STUFF/ORIGIN
mkdir ${SYSD}/DATA/NUMBERS/STUFF/USED
touch ${SYSD}/DATA/NUMBERS/STUFF/ORIGIN/1
touch ${SYSD}/DATA/NUMBERS/STUFF/ORIGIN/2
mv    ${SYSD}/DATA/NUMBERS/STUFF/ORIGIN/1 ${SYSD}/DATA/NUMBERS/STUFF/USED/1

#DATA/権限
chmod -R 770 ${SYSD}/DATA 

echo "finish"
