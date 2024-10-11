#!/bin/bash


docker ps

echo -e "\nproject dir: \n"

docker exec data-saving-container ls 

echo -e "\nstorage dir: \n"

docker exec data-saving-container ls storage

echo -e "\ndata.txt content: \n"

docker exec data-saving-container cat storage/data.txt

echo -e "database content: \n"

docker exec -it data-saving-container sqlite3 storage/data.db


exit


