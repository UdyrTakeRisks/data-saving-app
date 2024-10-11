#!/bin/bash


# runs in foreground to trace server logs and app status, to run in background use -d option

docker run --name data-saving-container -p 8000:8000 ahmeddalii/data-saving-app:latest





