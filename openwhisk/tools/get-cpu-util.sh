sum=0
count=0
while [ true ]
do
        # awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat)
        num=`awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1); }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat)`
        echo $num
        if [ 1 -eq "$(echo "7 < ${num}" | bc)" ]
        then
                # sum=$(( $sum + $num ))
                sum=`echo $sum + $num | bc`
                count=$(( $count + 1 ))
                avg=`echo $sum / $count | bc` # $(( $sum / $count ))
                echo "$count entries - avg: $avg"
        fi
done
