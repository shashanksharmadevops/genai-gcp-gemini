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
  default     = ["aiplatform.googleapis.com", 
                 "storage-component.googleapis.com", 
                 "cloudresourcemanager.googleapis.com",	
                 "analyticshub.googleapis.com", 
                 "bigquery.googleapis.com",
                 "bigqueryconnection.googleapis.com",
                 "bigquerydatapolicy.googleapis.com",
                 "bigquerymigration.googleapis.com",
                 "bigqueryreservation.googleapis.com",
                 "bigquerystorage.googleapis.com",
                 "cloudapis.googleapis.com",
                 "cloudresourcemanager.googleapis.com",
                 "cloudtrace.googleapis.com",
                 "dataform.googleapis.com",
                 "dataplex.googleapis.com",
                 "datastore.googleapis.com",
                 "logging.googleapis.com",
                 "monitoring.googleapis.com",
                 "servicemanagement.googleapis.com",
                 "serviceusage.googleapis.com",
                 "sql-component.googleapis.com",
                 "storage-api.googleapis.com",
                 "storage.googleapis.com"]
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

