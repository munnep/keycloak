from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC, PrivateSubnet, PublicSubnet, InternetGateway, NATGateway, ElbApplicationLoadBalancer
from diagrams.onprem.compute import Server
from diagrams.aws.storage import SimpleStorageServiceS3Bucket
from diagrams.aws.database import RDSPostgresqlInstance

# Variables
title = "VPC with 1 public subnet for the Keycloak instance"
outformat = "png"
filename = "diagram-keycloak"
direction = "TB"


with Diagram(
    name=title,
    direction=direction,
    filename=filename,
    outformat=outformat,
) as diag:
    # Non Clustered
    user = Server("user")

    # Cluster 
    with Cluster("aws"):
        with Cluster("vpc"):
            igw_gateway = InternetGateway("igw")
    
                            
            with Cluster("Availability Zone: eu-north-1a \n\n  "):
                # Subcluster 
                with Cluster("subnet_public1"):
                     ec2_keycloak_server = EC2("Keycloak server")

    # Diagram

    user >> ec2_keycloak_server

diag
