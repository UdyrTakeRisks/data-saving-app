#!/bin/bash



docker stop data-saving-container ; docker rm data-saving-container


# if $? returns 0 then the previous command executes without errors, -eq == equal

if [ $? -eq 0 ]; then
	echo "container stopped and removed successfully!"

else
	echo "Failed to stop or remove the container."

fi


# check active containers

docker ps
