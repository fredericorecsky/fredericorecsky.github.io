---
title: Bootstraping a new Google Cloud Organization using Terraform
published: false
---

# UPDATE - This is to bootstrap everything, that is not my case now

# A new day a new project but not a whole new infrastructure

Everyonce in a while every developer starts a side project. It can be to get some extra money or to learn a new technology, it does not matter. 
What really matters is this question: Would I need to recreate all the infrastructure this time again?

  -- Well, likely.
  
If you are a seasoned developer, you may have a set of tools to bootstrap your project on whatever infra you have, so here I am doing a step by step
on how I bootstrap a project on my infra of choice, Google Cloud on this case.  Also keep in mind that this text is about bootstrap and not what should 
be your tool or favorite cloud. The ideia should be the same if you are native k8s or running on AWS, whatever. 

# The Project

Well, this time the project is a simple website so a friend can write some texts and publish.  The goal is write less code as possible and work as well as it can.
Also we are foccused on the content and the user just want to edit some files to publish a text. For this case I will do a poor's man github pages 
using the resources I have and of course I could use github but my friend wants to publish whatever content as he wants, like 18+ for example. 

To mimic the Jekyll + github actions we are going to use:

* Google Cloud Project having: 
* Google Cloud Storage
* Google Cloud Build
* A github repository
* Jekyll 

This is the first time I am doing it so also I want to have a infra setup that I can reuse, so we add Terraform to be our infra control.
What I expect that Terraform will do for me:

* Create a Google Cloud Project
* Create a bucket to serve the site
* Create a Cloud Build Trigger so when the user edits the texts on github, it publishes it. 

Ideally after it is done I expect to forgot about it, except when I need it again and I hope it will be totally reusable.

## Start

So I already have a set Google Cloud account, so now I need to follow up the instructions on the 
official [Terraform Foundantion Project](https://github.com/terraform-google-modules/terraform-example-foundation)

Another thing I am doing is try to use only the browser. No special reason except that I want try.  So I started to follow up the terraform foundation. 

### Step 0

The goal is to have everything automated and running from cloud build. And this step it seems to be the only one made by hand. Until now I have being using 
few google cloud projects, mainly due employeers/customers policies so it feels strange start creating two projects, one for the project itself and other for CI/CD
but on other hand, *this is how it should be*. Both for modularity as well for security ( that does not mean that a monolitic cloud project is insecure but hard to harden ).

First step on step 0, running the checklist. Also on my side I started the browser cloud shell. Cute terminal on browser. And what a good surprise:

```
frederico@cloudshell:~ (XXXX)$ terraform -version
Terraform v1.2.3
on linux_amd64

Your version of Terraform is out of date! The latest version
is 1.2.4. You can update by downloading from https://www.terraform.io/downloads.html
frederico@cloudshell:~ (XXXX)$

# And it continues:

git --version
git version 2.30.2

# cool!
# So let's clone the Terraform Foundation Repository 

git clone https://github.com/terraform-google-modules/terraform-example-foundation.git

cd 0-bootstrap/
# Done
```
Now, just following the instructions on the Doc. When I renamed the file, I noted a button on gcp ui, "open editor". It opened something Visual studio code like, but on help it says: "Built with Eclipse Theia". 

So I am editing the file on it. It needed some information about my GCP account. I ended up following the entire thing and creating a new organization and everything so it does not mix with my old organizations. It helps organize the organizations on my organization. 
When I started to use GCP the overall organization was different ( I think it did not have folders ). This [link](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#cloud_platform_resource_hierarchy_and_iam_policy_hierarchy) is helpful to look and have a overview or update yourself.












