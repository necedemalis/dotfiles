clear

if [ $# != 0 ] 
then
        echo -n "Bitte geben sie den zu suchenden String ein: "
        read suche
        for i in $*
        do
                if test -r $i
                then
                        echo ""
                        echo "`grep -c $suche $i` Einträge in \"$1\"."
                        echo ""
                        echo "`grep $suche $i`"
                fi
        done
else
        echo "Es wurde keine Datei zum Suchen übergeben!"
fi
echo""
