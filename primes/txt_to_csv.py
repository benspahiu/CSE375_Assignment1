import re
import csv
import statistics

# Input/output file names
input_filename = "results/prime_tbb.txt"   # Change as needed
output_filename = "results/prime_tbb.csv"

# Regex patterns
header_n_pattern = re.compile(r"^-+ Output for n = (\d+) -+")
header_b_pattern = re.compile(r"^-+ Output for b = (\d+) -+")
time_pattern = re.compile(r"Time for \[\d+-\d+\]: ([\d.]+)")

# Storage for results
results = []

# Read the file
with open(input_filename, 'r') as file:
    lines = file.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()

    n = b = None
    times = []

    # Match header line
    if header_n_pattern.match(line):
        n = int(header_n_pattern.match(line).group(1))
        i += 1
    elif header_b_pattern.match(line):
        b = int(header_b_pattern.match(line).group(1))
        i += 1
    else:
        i += 1
        continue

    # Collect time lines
    while i < len(lines):
        time_line = lines[i].strip()
        time_match = time_pattern.match(time_line)

        if time_match:
            times.append(float(time_match.group(1)))
            i += 1
        elif time_line == '' or header_n_pattern.match(time_line) or header_b_pattern.match(time_line):
            break
        else:
            i += 1

    # Compute and store results
    if times:
        mean_time = statistics.mean(times)
        stddev_time = statistics.stdev(times) if len(times) > 1 else 0.0
        results.append([n if n is not None else "", b if b is not None else "", mean_time, stddev_time])

# Write to CSV
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["n", "b", "mean", "standard deviation"])
    writer.writerows(results)

print(f"Data successfully written to {output_filename}")