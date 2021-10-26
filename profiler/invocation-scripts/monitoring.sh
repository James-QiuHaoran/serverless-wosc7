FAAS_ROOT="/home/haoranq4/hqiu-owk/extended-faas-profiler"
time_stamp=$(date +%s%N | cut -b1-13)
systemd-cgtop > $FAAS_ROOT'/logs/systemd-cgtop_'$time_stamp'.txt'
