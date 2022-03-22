# Terraform running locally from docker

### Get the docker image

``` docker pull hashicorp/terraform:1.1.7```

 ```docker run hashicorp/terraform:1.1.7 plan```
 
 In case we changed the version, backup your state and run:

```terraform init -reconfigure```

### Connecting to github automatically 

[Reference](https://www.terraform.io/language/modules/sources#github)

Need to get authentication token on github, must use https for token. 

