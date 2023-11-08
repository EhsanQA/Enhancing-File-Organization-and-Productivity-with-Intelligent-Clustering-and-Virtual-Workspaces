import os
import shutil
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.metrics import pairwise_distances_argmin_min, silhouette_score

# Define the directory where synthetic files are generated
data_dir = "synthetic_data"
workspace_dir = "workspaces"

# Define the number of clusters (virtual workspaces)
num_clusters = 3

# Initialize a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Collect file names and their content
file_paths = []
file_content = []
for root, dirs, files in os.walk(data_dir):
    for file in files:
        file_paths.append(os.path.join(root, file))
        with open(os.path.join(root, file), "r", encoding='utf-8', errors="replace") as f:
            file_content.append(f.read())

# Vectorize the file content using TF-IDF
X = vectorizer.fit_transform(file_content)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(X)

# Calculate and print the Silhouette Score
silhouette_avg = silhouette_score(X, kmeans.labels_)
print(f"Silhouette Score: {silhouette_avg:.4f}")

# Calculate the Inertia score
inertia = kmeans.inertia_
print(f"Inertia Score: {inertia:.4f}")

# Create virtual workspaces
workspaces = {}
for i in range(num_clusters):
    workspace_name = f"Workspace {i + 1}"
    workspaces[workspace_name] = []

# Assign files to virtual workspaces
closest, _ = pairwise_distances_argmin_min(X, kmeans.cluster_centers_)
for i, closest_idx in enumerate(closest):
    file_path = file_paths[i]
    cluster_label = kmeans.labels_[i]
    workspace_name = f"Workspace {cluster_label + 1}"
    workspaces[workspace_name].append(file_path)

# Move files to their respective virtual workspaces in the specified workspace_dir
for workspace_name, files in workspaces.items():
    workspace_path = os.path.join(workspace_dir, workspace_name)  # Adjust the path here
    os.makedirs(workspace_path, exist_ok=True)
    for file_path in files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(workspace_path, file_name)
        shutil.move(file_path, destination_path)

print("Virtual workspaces created successfully.")