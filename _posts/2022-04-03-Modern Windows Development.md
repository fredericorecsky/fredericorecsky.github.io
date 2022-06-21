---
title: Modern Windows Workstation for Developers
---
# Using Windows on 202x ( WIP )

Windows is one of the historic and most used and installed O.S in the world. 
I had a high and lows relationship with it but still I always used it either at home or at work. 

Past years my home computer is an Mac and I have being using linux mainly on vms/containers or remote. 
Now I am back working on daily basis on a windows machine and compared to my previous experience ( Windows 8 ), 
windows 11 is a totally different experience. Mainly on my opinion now due to the Windows Linux Subsystem.

I am writing here how I set my machine and what kind of troubles I runned into. This text is mainly a working in progress
both on content as well as I am adjusting it to my daily needs.

## Configuring and using a Windows Workstation for Cloud Development

I mainly do software development for cloud, so usually I will run only subsets of the application locally, mainly on containers. 
The first thing I did was configure a way to use docker that is my main runtime now. 

The docker oficial desktop application is not something I like, but I use it on mac os because still easier ( but buggy ) than the other options. 
But the on the work computer the license of docker desktop is quite restrictive so I need somehow install docker vanilla and deal with it. So why not 
to run it on the WSL? I tried and in the end worked quite well. I followed the [official documentation](https://docs.microsoft.com/en-us/windows/wsl/install) 
and installed ubuntu and worked quite well. 

### Installing Docker

Just install it as you would do normally on ubuntu:

``` 
sudo apt-get update 
sudo apt-get install docker.io
sudo dockerd &
sudo chmod 666 /var/run/docker.sock
```

You may want to automate the last two commands, since every restart they need to run again, I don't mind run the commands after every restart.

#### Recurrent Problems on WSL

Sometimes the computer sleeps and when it wakes up, you may need to restart the whole WSL. Well it is windows after all. 

```
wsl --shutdown
```

Another thing is that you may get is random permissions or logon not allowed failures when trying to restart it. So you need to restart the 
vm-computing subsystem from windows:

```
# On PowerShell
# FIX the "Logon failure: the user has not been granted the requested logon type at this computer." 
# after a restart on wsl
Get-Service vmcompute | Restart-Service
```

