import sys

# Read lines from stdin
lines = sys.stdin.readlines()

# Initialize list to hold the first 3 values
values = []

# Loop through lines to find matching ones
for line in lines:
    if any(key in line for key in ["TOTAL EXECUTION TIME", "TIME PHASE 1", "TIME PHASE 2"]):
        value = line.strip().split('=')[-1].strip()
        values.append(value)

        # Stop after first 3 relevant lines
        if len(values) == 3:
            break

# Output to CSV format (to stdout or file)
print(','.join(values))