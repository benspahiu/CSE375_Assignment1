#!/bin/bash

# execs=("kmeans-serial")
# execs=("kmeans-serial" "kmeans-parallel" "kmeans-parallel1")
execs=("kmeans-serial" "kmeans-parallel")
# point_range=(100 1000 10000 100000)
point_range=(100 1000 10000)
dims=(3 6 9)
cluster_range=(4 8 12)

mkdir -p results

for num_points in ${point_range[@]}; do
  for dim in ${dims[@]}; do
    for clusters in ${cluster_range[@]}; do
      randoms=($RANDOM $RANDOM $RANDOM $RANDOM $RANDOM)
      dataset=dataset"$num_points"-"$dim"-"$clusters".txt
      echo Testing "$dataset"
      for exec in ${execs[@]}; do
        for random in ${randoms[@]}; do
          bin/"$exec" "$random" < kmeans-datasets/"$dataset" | python3 parse_to_csv.py >> results/"$exec".csv
        done
      done
    done
  done
done