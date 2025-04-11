import os
import blake3
import argparse
import multiprocessing
import threading
import time

# Constants
NONCE_SIZE = 6
HASH_SIZE = 10
RECORD_SIZE = NONCE_SIZE + HASH_SIZE

# Function to divide records into chunks
def split_chunks(records, num_chunks):
    chunk_size = len(records) // num_chunks
    chunks = [records[i:i + chunk_size] for i in range(0, len(records), chunk_size)]
    return chunks

# Function to generate hashes for a chunk of records
def hash_generation(records, result_queue, progress_callback, process_id):
    hashes = []
    total_records = len(records)
    for i, record in enumerate(records):
        nonce = record
        h = blake3.blake3(nonce).digest()[:HASH_SIZE]
        hashes.append((h, nonce))
        # Calculate progress percentage and print only at 100%
        if i == total_records - 1:
            progress_callback(process_id)
    result_queue.put(hashes)

# Function to perform parallel sorting using Timsort
def sorting_in_parallel(records, num_threads):
    def timsort_wrapper(records, start, end):
        records[start:end] = sorted(records[start:end], key=lambda x: x[0])
    chunk_size = len(records) // num_threads
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(records)
        thread = threading.Thread(target=timsort_wrapper, args=(records, start, end))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return records

# Function to write sorted hashes to a file
def hash_sort_writing(filename, sorted_hashes):
    with open(filename, 'wb') as f:
        for record in sorted_hashes:
            f.write(record[0] + record[1])

# Function to run the benchmark
def benchmarking(filename, hash_threads, sort_threads, write_threads, file_size, memory_size):
    # Calculate total number of records based on file size
    total_records = (file_size * 1024 * 1024) // RECORD_SIZE

    # Generate records
    records = [os.urandom(NONCE_SIZE) for _ in range(total_records)]

    # Divide records into chunks for multiprocessing
    process_chunks = split_chunks(records, hash_threads)

    # Start measuring hashgen time
    hashgen_start_time = time.time()

    # Start multiprocessing
    process_queue = multiprocessing.Queue()
    process_threads = []
    for i, chunk in enumerate(process_chunks):
        thread = threading.Thread(target=hash_generation, args=(chunk, process_queue, print_hash_progress, i))
        process_threads.append(thread)
        thread.start()

    # Wait for multiprocessing threads to complete
    for thread in process_threads:
        thread.join()

    # Collect hash results
    hashes = []
    for _ in process_threads:
        hashes.extend(process_queue.get())

    # Calculate hashgen time
    hashgen_time = time.time() - hashgen_start_time

    # Start sorting
    sort_start_time = time.time()
    sorted_hashes = sorting_in_parallel(hashes, sort_threads)
    sort_time = time.time() - sort_start_time

    # Write sorted hashes to a file
    write_start_time = time.time()
    hash_sort_writing(filename, sorted_hashes)
    write_time = time.time() - write_start_time

    # Print total hashgen, sort, and write times
    print(f"Hashgen time: {hashgen_time:.4f} seconds")
    print(f"Sort time: {sort_time:.4f} seconds")
    print(f"Write time: {write_time:.4f} seconds")

    # Calculate total time
    total_time = hashgen_time + sort_time + write_time
    print(f"Total time: {total_time:.4f} seconds")

# Function to print hashing progress
def print_hash_progress(process_id):
    print(f"[hashgen{process_id}]: 100.00% completed")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate hashes and sort them.')
parser.add_argument('-t', '--hash_threads', type=int, required=True, help='Number of hash threads')
parser.add_argument('-o', '--sort_threads', type=int, required=True, help='Number of sort threads')
parser.add_argument('-i', '--write_threads', type=int, required=True, help='Number of write threads')
parser.add_argument('-f', '--filename', type=str, required=True, help='Filename')
parser.add_argument('-s', '--file_size', type=int, required=True, help='File size in MB')
parser.add_argument('-m', '--memory_size', type=int, required=True, help='Maximum memory size in MB')
args = parser.parse_args()

# Run the benchmark
benchmarking(args.filename, args.hash_threads, args.sort_threads, args.write_threads, args.file_size, args.memory_size)
