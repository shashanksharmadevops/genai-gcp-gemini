variable "gcp-project-id" {
  description = "GCP project ID"
  default     = "<your-gcp-project-id>"
}

variable "gcp-sa-key-path" {
  description = "GCP Service Account Key Path "
  default     = "~/Documents/mysecrets" # path in your local
}

variable "gcp-services" {
  description = "GCP services api"
  type        = list(string)
  default     = ["aiplatform.googleapis.com", "storage-component.googleapis.com"]
}

variable "gcp-sa-roles" {
  description = "GCP roles for service account"
  type        = list(string)
  default     = ["roles/aiplatform.user", "roles/storage.objectViewer"]
}

variable "gcp-storage-bucket" {
  description = "GCP storage bucket"
  default     = "genai-demo-bucket"
}

