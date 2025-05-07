provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "crawler_sg" {
  name_prefix = "crawler-sg-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow access to backend on port 8083
  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    # Allow all outbound traffic (Important!)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "example" {
  ami           = "ami-084568db4383264d4"  # Ubuntu machine
  instance_type = "t2.micro"              # Free tier eligible
  key_name = "drmshft_fastapi"
  security_groups = [ aws_security_group.crawler_sg.name ]

  root_block_device {
    volume_size = 6  # 24 GB disk
    volume_type = "gp3"
  }

  lifecycle {
    ignore_changes = [ami]  # Prevents instance from recreating due to AMI changes
  }

  tags = {
    Name = "dreamshift-crawler"
  }

}

output "instance_public_ip" {
  description = "The public IP address of the EC2 instance"
  value       = aws_instance.example.public_ip
}
