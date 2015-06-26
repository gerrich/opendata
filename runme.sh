for i in `seq 0 11`; do echo $i; cat adresses_krasnodar.csv | tail -n+2 | ./geotest.py $i > result$i.txt; done
