output "ssh_keycloak_server" {
  value = "ssh ubuntu@${var.dns_hostname}.${var.dns_zonename}"
}

output "keycloak_dashboard" {
  value = "https://${var.dns_hostname}.${var.dns_zonename}"
}

output "keycloak_ip" {
  value = aws_eip.keycloak-eip.public_ip
}
