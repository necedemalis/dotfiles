clear

if [ $# == 0 ]
then
        doit=0
        echo "Es wurde keine Namensliste angegeben!"
else
        if test -r $1
        then
                doit=1
        else
                echo "Datei \"$1\" existiert nicht oder ist nicht lesbar."
                doit=0
        fi
fi

if [ $doit == 1 ]
then
        echo -n "Bitte geben sie den zu suchenden String ein: "
        read suche

        echo ""
        echo "`grep -c $suche $1` Einträge gefunden:"
        echo ""
        echo ""

        echo "`grep $suche $1`"
fi
echo ""
