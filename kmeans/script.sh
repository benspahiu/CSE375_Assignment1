#!/bin/bash

execs=("kmeans-serial")
# execs=("kmeans-parallel")

mkdir -p results

for exec in ${execs[@]}; do
  for((i = 1; i <= 10; i++)); do
    dataset=dataset"$i".txt
    echo Testing "$dataset" with "$exec"
    for((j = 1; j <= 5; j++)); do
      cat kmeans-datasets/"$dataset" | bin/"$exec" | python3 parse_to_csv.py >> results/"$exec".csv
    done
  done
done
echo Done
