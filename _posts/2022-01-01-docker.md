# Docker 

## Docker Cheat Sheet 

### List all containers

`docker container ls -a`

### Stop all containers
`docker container stop $(docker container ls -aq)`

### Remove all stopped containers

`docker container prune` 

### Container start-up status

`docker ps`
`docker inspect <container_name>|jq .[].HostConfig.RestartPolicy`

### Update container policy

`docker update --restart unless-stopped <container_name>`

### Restart docker service on mac os

`osascript -e 'quit app "Docker"'`
`open -a Docker`

