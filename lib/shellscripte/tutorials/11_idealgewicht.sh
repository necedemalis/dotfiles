#!/bin/bash
clear

echo -n "Bitte geben Sie Ihre Körpergröße in cm ein: "
read groesse

echo -n "Bitte geben Sie Ihr Gewicht ein: "
read gewicht

echo -n "Bitte geben Sie Ihr Geschlecht ein (m|w): "
read geschlecht

if [ $geschlecht == m ]
then
        ideal=`expr $groesse - 100`
        ideal=`expr $ideal \* 9`
        ideal=`expr $ideal \/ 10`
else
        if [ $geschlecht == w ]
        then
                ideal=`expr $groesse - 100`
                ideal=`expr $ideal \* 85`
                ideal=`expr $ideal \/ 100`
        else
                clear
                echo -e "\e[1;31mSie haben ein ungültiges Geschlecht.\e[0m"
                sleep 3
                bash 11_idealgewicht.sh
        fi
fi

echo ""
echo "Ihr Idealgewicht wäre $ideal kg."

differenz=`expr $gewicht - $ideal`

if [ $differenz -gt 0 ]
then
        echo "Sie haben $differenz kg Übergewicht: "
else
        if [ $differenz -lt 0 ]
        then
                differenz=`expr $differenz \* -1`
                echo "Sie haben $differenz kg Untergewicht: "
        else
                echo "Sie haben Idealgewicht."
        fi
fi
