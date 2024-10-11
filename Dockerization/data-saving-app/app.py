from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from service import store_in_db

# creating the application instance
app = FastAPI()

# serve static files like images to let fastapi load the image from assets
app.mount("/assets", StaticFiles(directory="Frontend/assets"), name="assets")

FRONTEND_PATH = "Frontend/index.html"


@app.get("/")
async def root():
    # return the html form page
    return FileResponse(FRONTEND_PATH)


@app.get("/health")
async def check_health():
    # root endpoint to check regularly the health of my application (monitoring)
    return {
        "message": "Data Saving Application is Working",
        "health": "Good"
    }


@app.post("/save-data")
async def save_data(name: str = Form(..., min_length=3, max_length=50),
                    message: str = Form(..., min_length=2, max_length=300)):
    try:
        # writing data received from form into file
        with open("storage/data.txt", "a") as file:
            file.write(f"Name: {name} \nMessage: {message} \n\n")

        # storing data into sqlite database asynchronously
        database_response = await store_in_db(name, message)

        return {
            "file message": "Data has been Saved Successfully in file",
            "database message": database_response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Occurred in Saving Data: {e}")
