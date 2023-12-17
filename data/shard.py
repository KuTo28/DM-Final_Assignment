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


filename = "heart_data.csv"
n_shards = 2

with open(filename, "r") as file:
    lines = file.readlines()

shards = partition_array(lines, n_shards)

for num, shard in enumerate(shards):
    with open(f"{num}_{filename}", "w") as file:
        file.writelines(shard)
