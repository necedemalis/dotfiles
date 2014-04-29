MATCH=""
DELAY=1

echo -n "Bitte Password eingeben: "
stty -echo
read CODE
stty echo
echo ""
echo ""
echo -n "Bitte wiederholen sie die Passwordeingabe: "
stty -echo
read CODEW
stty echo

if [ "$CODE" != "$CODEW" ]
then
        clear
        echo "Die beiden Eingaben sind nicht ident! "
        echo ""
        echo ""
        bash 10_lockscreen.sh
else
        while [ "$MATCH" != "$CODE" ]
        do
                clear
                sleep $DELAY
                echo -n "Bitte Password eingeben um den Bildschirm zu entsperren: "
                stty -echo
                read MATCH
                stty echo
                DELAY=`expr $DELAY \* 2`
        done
fi
echo ""
