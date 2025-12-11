# Ref: https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/blob/master/examples/simple_autopilot_public
# To define that we will use GCP
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.80.0" // Provider version
    }
  }
  required_version = "1.12.2" // Terraform version
}


provider "google" {
  project     = var.project_id
  region      = var.region
}

resource "google_container_cluster" "my-gke" {
  name     = "${var.project_id}-gke-k5"
  location = var.zone  // Use zone instead of region to reduce overhead
  // Standard mode (not Autopilot)
  remove_default_node_pool = true
  initial_node_count       = 1
  
  // Configure initial node pool to minimize SSD usage
  node_config {
    disk_type = "pd-standard"
  }
}

// Node pool with 2 nodes
resource "google_container_node_pool" "primary_nodes" {
  name       = "${var.project_id}-node-pool"
  location   = var.zone  // Use zone to match cluster
  cluster    = google_container_cluster.my-gke.name
  node_count = 2

  node_config {
    machine_type = "e2-small"
    disk_size_gb = 20
    disk_type    = "pd-standard"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
