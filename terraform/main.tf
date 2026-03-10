provider "aws" {
    region= "ap-south-1"
}
resource "aws_s3_bucket" "task_manager_bucket" {
  bucket = "ritika-task-manager-bucket"
}