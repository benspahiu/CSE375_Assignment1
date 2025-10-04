#!/bin/bash

# execs=("kmeans-serial")
execs=("kmeans-serial" "kmeans-parallel")

mkdir -p results

for((i = 1; i <= 10; i++)); do
  dataset=dataset"$i".txt
  echo Testing "$dataset"
  for((j = 1; j <= 5; j++)); do
    random="$RANDOM$RANDOM"
    for exec in ${execs[@]}; do
      cat kmeans-datasets/"$dataset" | bin/"$exec" "$random" | python3 parse_to_csv.py >> results/"$exec".csv
    done
  done
done
echo Done
