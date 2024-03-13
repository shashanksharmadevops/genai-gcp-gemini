resource "random_pet" "gcp-bucket-name" {
  keepers = {
    project_id = var.gcp-project-id
  }
  length    = 2 # number of words
  prefix    = "genai-demo-bucket"
  separator = "-"
}

resource "google_project_service" "project" {
  
  for_each = toset(var.gcp-services)
  project  = var.gcp-project-id
  service  = each.value
  timeouts {
    create = "30m"
    update = "40m"
  }
  disable_dependent_services = true
}

resource "google_storage_bucket" "gcp-gemini-storage-bucket" {
  name          = random_pet.gcp-bucket-name.id
  location      = "us-central1"
  force_destroy = true
  project       = var.gcp-project-id

  public_access_prevention = "enforced"
}

resource "google_service_account" "gcp-gemini-service-account" {
  account_id   = "gcp-gemini-demo"
  display_name = "GCP-Gemini-Demo"
  project      = var.gcp-project-id 
}

resource "google_project_iam_binding" "gc-gemini-demo-sa-role" {
    
    for_each = toset(var.gcp-sa-roles)
    project  = var.gcp-project-id
    role     = each.value
    members  = [
        "serviceAccount:${google_service_account.gcp-gemini-service-account.email}"
    ]
}

resource "google_service_account_key" "gcp-gemini-sa-key" {
    service_account_id = google_service_account.gcp-gemini-service-account.name
    public_key_type    = "TYPE_X509_PEM_FILE"
}

resource "local_file" "gcp-gemini-sa-key-download" {
    content  = base64decode(google_service_account_key.gcp-gemini-sa-key.private_key)
    filename = "${var.gcp-sa-key-path}/gcp-gemini-sa-key.json"
}