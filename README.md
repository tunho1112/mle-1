# mle

# deploy cluster k8s


# buid docker 

# Build the image
docker build -t diabetes-prediction-api:0.1 .

# Run the container
docker run -d --name diabetes-prediction -p 8080:8080 diabetes-prediction-api:0.1

## MLflow
```
# build
docker build -t mlflow:0.1 -f deployment/mlflow/Dockerfile --build-arg MLFLOW_VERSION=2.3.2 .
# run
docker run -d -p 5000:5000 mlflow:0.1
```

## Jenkins
```bash
03040bdac2ce48f3b43c7ac36e7a5526
```


// Google Kubernetes Engine
resource "google_container_cluster" "primary" {
  name     = "${var.project_id}-gke"
  location = var.region

  // Enabling Autopilot for this cluster
  enable_autopilot = true
}
