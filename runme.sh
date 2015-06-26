#!/bin/bash

src=adresses_saratov.csv
#src=adresses_krasnodar.csv
for i in `seq 0 11`; do echo $i;
  cat ${src} |\
  tail -n+2 |\
  ./geotest.py $i > ${src}.${i}.out;
done
