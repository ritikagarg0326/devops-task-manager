
resource "aws_s3_bucket" "task_manager_bucket" {
  bucket = var.bucket_name
  force_destroy = true
}
resource "aws_ecr_repository" "task_manager_repo" {
  name = "task-manager-repo"

  image_scanning_configuration {
    scan_on_push = true
  }
}
resource "aws_instance" "task_manager_ec2" {
  ami           = "ami-04680790a315cd58d"
  instance_type = "t3.micro"
  subnet_id = "subnet-0151f42da8b3517fc"
  tags = {
    Name = "task-manager-ec2"
  }
}