sed 's/,/ /g' $1 | awk 'NR > 17 {print $1","$2","$3","$4}' > ../data/$1
