# Easy-Donate-API

The API is developed using Python's FastAPI framework.

## Prerequisites

- Python 3.5 or above  
- Browser or Postman app to test the API

## Starting the server

1. Clone this repository.  
2. Create a virtual env inside the project folder (if needed).  
3. Run the command `pip install -r requirements.txt` in the terminal pointed inside the root directory.  
4. To Start the server, run `uvicorn main:app --reload` in ther terminal.  

## Testing the server

- In the browser, check http://127.0.0.1:8000/docs for the endpoints in which the same can be tested.
- To check in postman, use http://127.0.0.1:8000/{endpoints} url to send requests with required parameters.
