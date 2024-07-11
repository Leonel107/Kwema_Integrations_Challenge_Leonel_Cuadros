To run the program's API you must:

- Activate the virtual environment: Access the files folder ("Kwema_Integrations_Challenge_Leonel_Cuadros") 
and run the cmd program.Then run the command "venv\Scripts\activate", Windows, and the virtual environment 
will be activated.

- In the virtual environment, run the command "uvicorn main:kwema --port 5000"

- Then open the Browser and put the following URL: "http://localhost:5000/docs#/".
The endpoints will appear in this URL.

- Go to the "GET/user-insights" endpoint and execute the "Try it out" button and then the "Run" button to view 
the data obtained from the profiles used as an example.

- The data entered has been obtained through web scraping, through the "Kwema.ipynb" file. Where the process to 
obtain the requested data is detailed step by step.