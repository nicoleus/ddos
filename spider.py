#!/bin/sh
#colour
R='\033[1;31m'
B='\033[0;34m'
C='\033[0;36m'
G='\033[1;32m'
W='\033[1;37m'
Y='\033[0;33m'
Y2='\033[1;33m'
clear

   echo ""
   echo  "    \033[31m ██████ ███████ ██ \033[32mnico \033[31m██ ██████ ██████ \033[0m"
   echo  "    \033[31m ██     ██   ██ ██      ██ ██     ██     \033[0m"
   echo  "    \033[31m ██████ ███████ ██ ███████ ██████ ██     \033[0m"
   echo  "    \033[31m     ██ ██      ██ ██   ██ ██     ██     \033[0m"
   echo  "    \033[31m ██████ ██      ██ ███████ ██████ ██   v.1  \033[m"
echo "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
echo -n "\033[0;36m[*] Target Url : "
read asu
if [ ! -z $asu ]
then
echo "[*] Scanning..."
nmap -p 80 --script=http-exif-spider -sV $asu
echo -n "\033[1;31m[${W}press ENTRE to go back${R}]~#: " $nico
read ENTRE
$PREFIX/share/nicoleus/.modules/.smbscan
else
echo "\033[31m[${W}"!"${R}"] please Enter target  Url'\'IP${W}'!' " "
sleep 5
$PREFIX/share/nicoleus/.modules/.smbscan
fi

