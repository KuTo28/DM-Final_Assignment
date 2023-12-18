import sys
import os


def partition_array(arr, x):
    # Calculate the size of each partition
    partition_size = len(arr) // x
    remainder = len(arr) % x  # Calculate the remainder

    # Use list comprehension to create partitions
    partitions = [
        arr[i : i + partition_size]
        for i in range(0, len(arr) - remainder, partition_size)
    ]

    # Add the remaining elements as a separate partition
    partitions.extend(
        [
            arr[i : i + remainder]
            for i in range(len(arr) - remainder, len(arr), remainder)
        ]
    )

    return partitions


if len(sys.argv) != 3:
    print("This cli takes two positional arguments <filepath> <n_shards>")
    exit(1)

filepath = sys.argv[1]
n_shards = int(sys.argv[2])

with open(filepath, "r") as file:
    lines = file.readlines()

filename = os.path.basename(filepath)
filedir = os.path.dirname(filepath)

shards = partition_array(lines, n_shards)

for num, shard in enumerate(shards):
    with open(f"{filedir}//{num}_{filename}", "w") as file:
        file.writelines(shard)
