terraform {
  backend "s3" {
    bucket = "ritika-task-manager-bucket"
    key    = "terraform/state/terraform.tfstate"
    region = "us-east-1"
  }
}