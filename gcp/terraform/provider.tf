terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.18.0"
    }
    random = {
      source = "hashicorp/random"
      version = "3.6.0"
    }
  }
}

provider "google" {
  # Configuration options
  region      = "us-central1"
}

provider "random" {
  # Configuration options
}