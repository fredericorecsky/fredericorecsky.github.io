---
title: VirtualBox Random Notes
---
# VirtualBox 

## VirtualBox Headless

Using virtualbox machines headless. Useful when you run your 
images on a remote server or even a localserver without graphical UI.

```shell
VBoxManage list vms 
VBoxHeadless -s servername 
VBoxManage startvm servername --type headless
```

These days I mostly use docker or k8s but for some stuff ( low level or 
to test linux distributions ) I prefer the old style vms ;)
