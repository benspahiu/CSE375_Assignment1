import numpy as np
from sklearn.datasets import make_blobs

# Configuration
point_range = [100, 1000, 10000, 100000]
dimensions_range = [3,6,9]
cluster_range = [4, 8, 12]
max_iterations = 200
output_dir = "kmeans-datasets"


for num_points in point_range:
  for dim in dimensions_range:
    for num_clusters in cluster_range:
      centers = num_clusters

      # Generate synthetic dataset
      X, _ = make_blobs(n_samples=num_points,
                        n_features=dim,
                        centers=centers,
                        random_state=dim)  # use dim as seed for variation

      # Prepare header
      # Format: num_points dimensions clusters max_iterations label_bool
      header = f"{num_points} {dim} {num_clusters} {max_iterations} 0"

      # Write to file
      output_path = output_dir + f"/dataset{num_points}-{dim}-{num_clusters}.txt"
      with open(output_path, "w") as f:
          f.write(header + "\n")
          for point in X:
              line = " ".join(f"{val:.4f}" for val in point)
              f.write(line + "\n")

print(f"Datasets saved in '{output_dir}/'.")