import csv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [list(map(float, row)) for row in reader]

def average_rows(rows):
    n = len(rows)
    return [sum(row[0] for row in rows) / n]

def compute_speedups(file1, file2, output_file, group_size=5):
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    num_rows = min(len(data1), len(data2))
    output = []

    for i in range(0, num_rows, group_size):
        group1 = data1[i:i+group_size]
        group2 = data2[i:i+group_size]

        if len(group1) < group_size or len(group2) < group_size:
            break  # Skip incomplete final group

        avg1 = average_rows(group1)
        avg2 = average_rows(group2)

        # Avoid division by zero
        speedups = [round(a / b, 4) if b != 0 else float('inf') for a, b in zip(avg1, avg2)]
        output.extend(speedups)

    # Write to output CSV
    with open(output_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(output)

    print(f"Done!")

# Example usage:
compute_speedups('results/kmeans-serial.csv', 'results/kmeans-parallel.csv', 'speedup.csv')
for i in range(1, 8):
  compute_speedups('results/kmeans-serial.csv', f'results/kmeans-parallel{i}.csv', 'speedup.csv')