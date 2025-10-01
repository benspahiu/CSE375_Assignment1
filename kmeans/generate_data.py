import numpy as np
from sklearn.datasets import make_blobs

# Configuration
num_points = 1000
dimensions_range = range(3, 11)
max_iterations = 200  # Not used directly but reserved for clustering
output_dir = "kmeans-datasets"


for dim in dimensions_range:
    num_clusters = dim + 1  # or any other heuristic
    centers = num_clusters

    # Generate synthetic dataset
    X, _ = make_blobs(n_samples=num_points,
                      n_features=dim,
                      centers=centers,
                      random_state=dim)  # use dim as seed for variation

    # Prepare header
    # Format: num_points dimensions clusters samples_per_cluster dummy_label_index
    samples_per_cluster = num_points // num_clusters
    header = f"{num_points} {dim} {num_clusters} {samples_per_cluster} 0"

    # Write to file
    output_path = output_dir + f"/dataset{dim}.txt"
    with open(output_path, "w") as f:
        f.write(header + "\n")
        for point in X:
            line = " ".join(f"{val:.4f}" for val in point)
            f.write(line + "\n")

print(f"Datasets saved in '{output_dir}/' for dimensions 3 through 10.")