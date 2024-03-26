# Docker workshop
## Commands to run the demo

### Without docker compose
```bash
# Build node app image
docker build -t node-client-image ./node_client

# Build python app image
docker build -t pyserver-image ./python_server

# Start python app container
docker run -it --name pyserver pyserver-image
# This will start a http server.
# Since we passed `-it`, the server will log to this terminal.
# You can run `-d` to run detached.

# Start node app container
docker run -it --name node-client node-client-image
# Notice the error `TypeError: fetch failed`.
# The host name pyserver cannot be resolved because we have not created 
# a network for the containers.

# Create a network
docker network create mynetwork

# Connect the containers to the network
docker network connect mynetwork pyserver
docker network connect mynetwork node-client

# Start the node-client container again
docker start -i node-client
# Notice the process runs to completion and prints "some data" to the console.
# The node-client container successfully made a http request to the pyserver.
# You may run the last command as many times as you want to see the same output.
# It is "equivalent" to running:
node app.js
# Since this is what we configured the container to do.

# To clean up
# Stop and remove containers we created
docker stop pyserver # or control-c
docker rm pyserver
docker rm node-client

# Remove images we created
docker image rm node-client-image
docker image rm pyserver-image

# Remove the network
docker network rm mynetwork

# To clear builder cache
docker builder prune -f
```

### With docker compose
```bash
# Create and start services
docker compose up # in the same directory as 'compose.yml'
# Notice all the logs are on the same terminal and you can see the same thing as above.
# To stop enter control-c

# Remove all (removes containers, images, network)
docker compose down --rmi all

# To clear builder cache
docker builder prune -f

# Note how many commands the docker compose configuration has saved us
```
