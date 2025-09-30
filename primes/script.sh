#!/bin/bash

files=("prime_dynamic")
n_range=(1000 10000 100000 1000000)
t_range=(8)
# n_range=(1000000)
# for file in ${files[@]}; do
#   make clean_"$file"
#   make "$file"
#   txt_file="results/$file.txt"
#   echo "===== Output for prime_tbb =====" >> "$txt_file"

#   for ((n=1000; n<=1000000; n*=10)); do
#     echo "Running: ./$file -n $n"
    
#     # Header
#     echo "----- Output for n = $n -----" >> "$txt_file"

#     # Run and append output
#     for((i=0; i<5; i++)); do
#       "./$file" -n "$n" >> "$txt_file"
#     done

#     echo "" >> "$txt_file"  # Add a blank line between results
#   done

#   echo "Done. Results saved in $txt_file."
# done
for file in ${files[@]}; do
  make clean_"$file"
  make "$file"
  txt_file="results/$file.txt"
  echo "===== Output for $file =====" >> "$txt_file"

  # n=$n_range
  for t in ${t_range[@]}; do
    for n in ${n_range[@]}; do
      for ((b=1; b<=n; b*=2)); do
        echo "Running: ./$file -n $n -b $b -t $t"
        
        # Header
        echo "----- Output for n = $n, b = $b, t = $t -----" >> "$txt_file"

        # Run and append output
        for((i=0; i<5; i++)); do
          "./$file" -n "$n" -b "$b" -t "$t" >> "$txt_file"
        done

        echo "" >> "$txt_file"  # Add a blank line between results
      done
    done
  done

  echo "Done. Results saved in $txt_file."
done