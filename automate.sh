#!/bin/bash

# Define the list of values for each command line argument
memory_sizes=(128)
hash_threads=(1 4 16)
sort_threads=(1 4 16)
write_threads=(1 4 16)

# Initialize a counter for the output file names
counter=1

# Iterate over each combination of command line arguments
for mem_size in "${memory_sizes[@]}"; do
    for ht in "${hash_threads[@]}"; do
        for st in "${sort_threads[@]}"; do
            for wt in "${write_threads[@]}"; do
                # Execute the command with the current combination of arguments
                ./hashgen.py -t "$ht" -o "$st" -i "$wt" -m "$mem_size" -s 1024 -f "output$counter.bin"
                ((counter++))
            done
        done
    done
done

