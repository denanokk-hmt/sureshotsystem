#!/bin/bash -evx

#ソース管理しないディレクトリ
mkdir ../BACKUP
mkdir ../DATA
mkdir ../DATA/NUMBERS
mkdir ../DATA/ORG_LV1-3
mkdir ../DATA/ORG_LV1-3/LV1
mkdir ../DATA/ORG_LV1-3/LV2
mkdir ../DATA/ORG_LV1-3/LV3
mkdir ../DATA/STUFF
mkdir ../DATA/STUFF/LOGIN
mkdir ../DATA/STUFF/LOGIN/LV1
mkdir ../DATA/STUFF/LOGIN/LV2
mkdir ../DATA/STUFF/LOGIN/LV3
mkdir ../DATA/STUFF/USERS
mkdir ../DATA/STUFF/USERS/LV1
mkdir ../DATA/STUFF/USERS/LV2
mkdir ../DATA/STUFF/USERS/LV3
mkdir ../IMG
mkdir ../LOCK
mkdir ../LOG
mkdir ../RCV
mkdir ../SAMPLE
mkdir ../SESSION
mkdir ../SND
mkdir ../TMP

#作成したディレクトリの権限変更
chmod -R 770 ../BACKUP/
chmod -R 770 ../IMG/
chmod -R 770 ../LOCK/
chmod -R 770 ../LOG/
chmod -R 770 ../RCV/
chmod -R 770 ../SAMPLE/
chmod -R 770 ../SESSION/
chmod -R 770 ../SND/
chmod -R 770 ../TMP/

#初期スタッフ登録
cp ./initial_stuff_login ../DATA/STUFF/LOGIN/LV1/1_login_20170101010101 
cp ./initial_stuff_login ../DATA/STUFF/LOGIN/LV2/1_login_20170101010101 
cp ./initial_stuff_login ../DATA/STUFF/LOGIN/LV3/1_login_20170101010101 
cp ./initial_stuff_users ../DATA/STUFF/USERS/LV1/1_stuff_20170101010101
cp ./initial_stuff_users ../DATA/STUFF/USERS/LV2/1_stuff_20170101010101
cp ./initial_stuff_users ../DATA/STUFF/USERS/LV3/1_stuff_20170101010101

#スタッフの初期採番
mkdir ../DATA/NUMBERS/STUFF
mkdir ../DATA/NUMBERS/STUFF/ORIGIN
mkdir ../DATA/NUMBERS/STUFF/USED
touch ../DATA/NUMBERS/STUFF/ORIGIN/1
touch ../DATA/NUMBERS/STUFF/ORIGIN/2
mv ../DATA/NUMBERS/STUFF/ORIGIN/1 ../DATA/NUMBERS/STUFF/USED/1

#DATA/権限
chmod -R 770 ../DATA 

echo "finish"
