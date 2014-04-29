clear
echo `touch lotto_temp`
rnd=$((RANDOM % 49 + 1))
i=0

while [ $i -lt 6 ]
do
        while [ `grep -c $rnd lotto_temp` -gt 0 ]
        do
                rnd=$((RANDOM % 49 + 1))
        done
        echo $rnd >> lotto_temp
        i=`expr $i + 1`
done
echo `sort -n lotto_temp`
echo `rm lotto_temp`
echo "
