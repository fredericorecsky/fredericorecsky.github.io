# Terraform running locally from docker

### Get the docker image

``` docker pull hashicorp/terraform:1.1.7```

 ```docker run hashicorp/terraform:1.1.7 plan```
 
 In case we changed the version, backup your state and run:

```terraform init -reconfigure```

