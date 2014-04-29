clear
echo -n "Bitte geben Sie Ihre Lieblings-Obstsorte ein:"
read obst

if test -z $obst
then
        echo "Sie haben keine Obstsorte angegeben."
else
        echo "So so, Sie mögen also gerne $obst."
fi
echo""

