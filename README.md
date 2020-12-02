# Python Contact Book

This application replicates a contact book and is intended to be utilized via the command line. Currently, the application allows users to read, create, and delete contacts from a locally run PostgreSQL database.

## Getting Started

To run the application locally, make sure to have pipenv installed on your machine and fork and clone this repository. Once the repo has been cloned locally, run `pipenv install` to install dependencies listed in the Pipfile. Start your Postgres server on your machine and update the user and password on line 6 in app.py to match that of your local Postgres database.


Then run the in the command line - python app.py or python(#) app.py depending on what version of python is installed, to start the app.

```

## Development

The model as of now remains simple, consisting of just a first & last name, as well as a phone number. The application itself functions as a class and create, read and delete are all methods called within the App class. I then created my database connection and templated myodel.

There is both an option to search for a specific contact as well as list all contacts in the book. I then created add functionality and finished with delete.

## Unsolved Problems

In the future I would like to add edit functionality so that you can update existing contacts. 


## Technologies Used

- Python
- PeeWee (psycopg2-binary, autopep8)
- PostgreSQL
