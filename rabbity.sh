#! /bin/bash
#Colors
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
Purple="\033[0;35m"
Cyan="\033[0;33m"
Cafe="\033[0;33m"
Fiuscha="\033[0;35m"
blue="\033[1;34m"
nc="\e[0m"
echo -e "$blue by JOE.$nc"

#Installation
sleep 1
echo -e "Checking Installation $nc"
echo -e "Checking Connection Completed [$blue✓$nc] $nc"
sleep 1
clear
#Startup
echo -e "$Cyan"
echo "      █▀█                                  █▀█"
echo "     █   ▀█                              █▀   █"
echo "    █     ▀▀█                          █▀▀     █"
echo "   █        ▀█                        █▀        █ "
echo "   █          █      Rabbity V0.0    █          █ "
echo "   █           █                    █           █"
echo "   ▀█          ▀█                  █▀          █▀"
echo "    ▀█          ▀█                █▀          █▀"
echo "     ▀█          ▀█              █▀          █▀ "
echo "       █           █            █           █"
echo "        █          █▀▀▀▀▀▀▀▀▀▀▀▀█          █" 
echo "        ▀█                               █▀    I- launch server(s)" 
echo "         █        ▀               ▀      █     II- serpent client"
echo "        █▀         ▀             ▀       ▀█    III- galaxy client" 
echo "      █▀        ███ ▀           ▀ ███     ▀█   IV- others"
echo "    █▀         █   █     ██      █   █     ▀█  V- close the door"
echo "   █	        ▀▀▀	 	  ▀▀▀        █"
echo "   █         				     █"
echo "    █	           ████████	            █"
echo "    ██         	    ██		           ██"
echo "     ███                                 ███"
echo "        █████████████████████████████████ "
read -p ":> " 
sleep 1
clear
if [[ "$REPLY" == 'I' ]]; then
    source env/bin/activate
    
    echo "choose job from? [s/g]: "
    read job
    case "$job" in 
	    S|s) source env/bin/activate ; cd rpcServer ; python3 args.py -q "serpent"
		 ;;
	    G|g) source env/bin/activate ; cd rpcServer ; python3 args.py -q 'galaxy'
		 ;;
	    *)   exit
		 ;;
    esac
elif [[ "$REPLY" == 'II' ]]; then
	 . env/bin/activate ; cd rpcClient ; python3 args.py -o "serpent"
elif [[ "$REPLY" == 'III' ]]; then
	 echo "'$REPLY'"
elif [[ "$REPLY" == 'IV' ]]; then
	 echo "'$REPLY'"
else
	exit
fi

