#!/bin/bash

execs=("kmeans-serial")
datasets=("dataset1.txt" "dataset2.txt")

mkdir -p results

for exec in ${execs[@]}; do
  for dataset in ${datasets[@]}; do
    echo Testing "$dataset" with "$exec"
    for((i = 1; i <= 5; i++)); do
      cat kmeans-datasets/"$dataset" | ./"$exec" | python3 parse_to_csv.py >> results/"$exec".csv
    done
  done
done
echo Done
