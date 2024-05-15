variable "tag_prefix" {
  description = "default prefix of names"
}

variable "keycloak_admin_password" {
  description = "Password for the admin user to login to keycloak"
}


variable "region" {
  description = "region to create the environment"
}

variable "vpc_cidr" {
  description = "which private subnet do you want to use for the VPC. Subnet mask of /16"
}

variable "public_key" {
  type        = string
  description = "public to use on the instances"
}

variable "dns_hostname" {
  description = "DNS hostname"
}

variable "dns_zonename" {
  description = "DNS zonename"
}

variable "certificate_email" {
  description = "email address to register the certificate"
}