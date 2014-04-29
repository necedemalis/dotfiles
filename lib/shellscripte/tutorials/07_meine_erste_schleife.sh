clear

x=1
while [ $x -le 10 ]
do
        echo "x=$x"
        x=`expr $x + 1`
done
