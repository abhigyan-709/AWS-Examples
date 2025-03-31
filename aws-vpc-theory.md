# What is VPC 
VPC is an isolated cloud server, in the clouds. Its also know as Virtual Private Cloud, which generally isolates the work and services from the public cloud in the AWS Servers.

1. VPC Provide more control over interaction with the servers
2. they are also having more security as they are totally isloated from the external or public spaces
3. VPC is logically isolated network, that resembles like you are having your own network in your datacenter
4. VPC provide many componets that you can work on, like Internet Gateway, public and private subnets etc

## core components of the AWS VPC
VPC is having major core components as described below

1. Internet Gateway (IGW) - its a gateway that connects your VPC to public internet.
2. VPN gateway - this is the private gateway to securely connects with your external network like on premises data centers
3. Route Tables - it determines the traffic within the VPC
4. NAT Gateways - allows private instances to connect with the services outside the VPC
5. NACL's (Network access control list) - this operates as a stateless virtual firewall, which operates at subnet level, with allow and deny rules
6. Security Group - this is used at the instance level and works as statefull virtual firewall, which have only allow rules
7. Public Subnets - it connects with the IGW and provide access to the public resources using public IPV4, you can say it allows instances to have the public instances.
8. Private Subnets - it disallows the instance to have a public ip address
9. VPC Endpoints - privately connects to the AWS Support Services
10. VPC Peering - its the way to connect to the one VPC to another VPC


## Key features of the VPC
- VPC's are region specific, and they dont span regions
- you can use VPC peering to connect to the other VPC 

AWS_CLI_AUTO_PROMPT=on-partial
