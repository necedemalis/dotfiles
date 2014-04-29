clear

echo -n "Welche Zahlen wollen sie addieren?:"
read z1
echo "a=$z1"
read z2
echo "b=$z2"

echo ""

erg=`expr $z1 + $z2`
echo "$z1+$z2 ist $erg!"
echo ""
