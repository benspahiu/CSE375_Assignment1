#!/bin/bash

output_file="prime_results.txt"

for ((n=1000; n<=1000000; n*=10)); do
  echo "Running: ./prime -n $n"
  
  # Header
  echo "----- Output for n = $n -----" >> "$output_file"

  # Run and append output
  for((i=0; i<5; i++)); do
    ./prime -n "$n" >> "$output_file"
  done

  echo "" >> "$output_file"  # Add a blank line between results
done

echo "Done. Results saved in $output_file."