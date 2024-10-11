
Platform: Manjaro (Arch. linux)

sqlite3 version: 3.46.1

python version: 3.12.5

pip version: 24.2

fastapi-cli version: 0.0.5

uvicorn version: 0.31.0

-----------------------------------------------------------------------------------------------------

Two ways to run the fastapi application:

 1- Run the application on your local environment (venv) 
    
    - In the project dir run: 
    
    	$ uvicorn app:app --reload or fastapi dev app.py (dev mode) or fastapi run (production mode)
    	
    - Make sure your have sqlite3 on your machine
    
    - Write data in the form, it should reflect on data.txt and data.db
    
    
 2- Run the run-container.sh script to run the docker image pushed on dockerhub (platform-independent environment)
 
 	you will have one docker container working then try saving data it should reflect on data.txt 
 	
 	and data.db so run the script check-data.sh to verify that data is being stored successfully and 
 	
 	you will be prompted to sqlite3 shell so do the following:
 	
 		sqlite> .tables
 		sqlite> .schema messages
 		sqlite> select * from messages;
 		sqlite> .exit	
 		
 		
 	if you want to stop and remove the container just run the remove-container.sh script, all data entered from
 	
 	container will be stored but once container removed the data will be removed as it needs volume binding.
 	
 	
 	NOTE: Don't forget to let the scripts executable by running the command below:
 	
 	$ chmod +x <script-name>.sh
 	
 	run the scripts using: $ bash <script-name>.sh or $ ./<script-name>.sh
    
    
    Thanks for reading!
    
    
    
    	
