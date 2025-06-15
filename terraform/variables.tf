variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "lambda_memory" {
  description = "Lambda memory (MB)"
  type        = number
  default     = 128
}

variable "lambda_timeout" {
  description = "Lambda timeout (sec)"
  type        = number
  default     = 10
}
