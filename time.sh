test -e doing && echo UNEXPECTED STATE && exit 1

now() { date +%s; } # <- `;` is necessary!

t=`now`
echo $1 $t > doing
echo "Timing for $1 started...(press Enter to stop)"
read # wait key press

dt=$((`now` - $t))
echo "$dt secs. bye!"
echo $1 $dt $t >> timetrack
rm doing
