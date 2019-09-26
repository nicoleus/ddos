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


#code
clear
echo " "
echo $G"  ██ ███    ██ ███████  █████ "
echo $G"  ██ ████   ██ ██      ██  ████"
echo $G"  ██ ██ ██  ██ █████   ██ ██ ██"
echo $G"  ██ ██  ██ ██ ██      ████  ██"
echo $G"  ██ ██   ████ ██$R Termux $G█████ Gathering by Nicoleus"
echo $Y2
echo  "------------------(main menu)-------------------"
echo
echo $B"[$R"01"$B]$G Inf0ga-----------> em@il ghather "
echo $B"[$R"02"$B]$G Nikto------------> web server scaner "
echo $B"[$R"03"$B]$G Red hawk---------> inf0rmation gathering"
echo $B"[$R"04"$B]$G Recon-ng---------> rec0nnaissance"
echo $B"[$R"05"$B]$G The harvester----> subd0main-emails gather"
echo $B"[$R"06"$B]$G Cms detection----> CMS detection"
echo $B"[$R"07"$B]$G Metag0file-------> files gathering to0l" 
echo $B"[$R"00"$B]$G BACK "  
echo $B"[$W"XX"$B]$G EXIT "
echo " "
echo -n $R"[$W"Inf0rmation Gathering t00ls"$R]$W"~"$R"'#': 
read zaki
#Inf0ga
if [ $nico = "1" ] || [ $nico = "01" ];
then
clear
figlet -f small "           INF0GA"
echo $C "Exemple $R[$W google.com$R ] "
echo -n $R "Target or website$Y : " 
read site
python2 $PREFIX/share/HORAS/.modules/.Infoga/infoga.py --target $site --source all 
echo -n $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#Nikto
elif [ $nico = "2" ] || [ $nico = "02" ];
then 
echo
clear
figlet -f small "           NIKT0"
echo $C "Exemple $R[$W google.com$R ] "
echo -n $R "Target or website$Y : " 
read site
perl $PREFIX/share/HORAS/.modules/.nikto/program/nikto.pl -Tuning -Plugins -Userdbs -url $site -C all -port 80 -output $HOME/EasY_HaCk-results/nikto.txt
echo $G"see HORAS folder for the$W nikto.txt$G output"
echo -n $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#Red hawk
elif [ $nico = "3" ] || [ $nico = "03" ];
then 
clear
php $PREFIX/share/HORAS/.modules/.RED_HAWK/rhawk.php
echo -n $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#Recon-ng
elif [ $zaki = "4" ] || [ $zaki = "04" ];
then 
clear
python2 $PREFIX/share/HORAS/.modules/.recon-ng/recon-ng --no-check 
echo -n $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#The harvester
elif [ $nico = "5" ] || [ $nico = "05" ];
then 
echo
echo $C "Please input the target website "
echo -n $R "Target or website$Y : " 
read site
python2 $PREFIX/share/HORAS/.modules/.theHarvester/theHarvester.py -d $site -b all -l 1000 -s 300 -f $HOME/HORAS-results/theHarvester-results.html
echo $G"see HORAS folder for the$W theHarvester$G output if exist !"
echo -n  $R"Press" ENTRE to back" " 
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#Cms detection
elif [ $nico = "6" ] || [ $nico = "06" ];
then 
echo
clear
python3 $PREFIX/share/HORAS/.modules/.CMSeeK/cmseek.py
echo -n  $R"Press" ENTRE to back" "
read ENTRE 
$PREFIX/share/HORAS/.modules/.inf0
#Metag0file
elif [ $nico = "7" ] || [ $nico = "07" ];
then 
echo
echo -n $R " Target or website$Y : " 
read site
python2 $PREFIX/share/HORAS/.modules/.metagoofil/metagoofil.py -d $site -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -l 2000 -n 500 -o $HOME/EasY_HaCk-results/metagoofil -f $HOME/EasY_HaCk-results/metagoofil/metagoofil-results.html
echo -n  $R"Press" ENTRE to back" "
read ENTRE
$PREFIX/share/HORAS/.modules/.inf0
#Back 
elif [ $zaki = "00" ] || [ $zaki = "0" ];
then
clear
echo "HORAS "
sleep 1
clear
$PREFIX/share/EasY_HaCk/.modules/.web
elif [ $nico = "X" ] || [ $nico = "x" ] || [ $nico = "xx" ] || [ $nico = "XX" ] ;
then
clear
echo "HORAS LAE KU!! (0_0)"
sleep 1
exit 
else
clear
echo $Y" Wrong Input..."
sleep 1
sh $0
fi
#end

