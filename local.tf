locals {
  az1 = "${var.region}a"
  certificate_full_chain = "${acme_certificate.certificate.certificate_pem}${acme_certificate.certificate.issuer_pem}"
}