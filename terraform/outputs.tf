output "api_endpoint" {
  description = "Invoke URL"
  value       = "https://${aws_api_gateway_rest_api.api.id}.execute-api.${var.aws_region}.amazonaws.com/prod/resize"
}
