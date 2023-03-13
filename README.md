# Django CRM Application

This is a simple CRM (Customer Relationship Management) application built using Django framework. It allows users to login, add new customers and delete existing ones.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3
- Django 4.1.7
- asgiref 3.6.0
- crispy-bootstrap5 0.7
- django-crispy-forms 2.0
- sqlparse 0.4.3
- tzdata 2022.7

## Getting Started

1. Clone the repository:

    git clone https://github.com/wellrccity/djangoCRM

2. Install the required dependencies:

    pip install -r requirements.txt

3. Migrate the database:

    python manage.py migrate

4. Create a superuser:

    python manage.py createsuperuser

5. Run the development server:

    python manage.py runserver

6. Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

7. Login using the superuser credentials created in step 4.

## Usage

After logging in, you can see the following functions:

- http://127.0.0.1:8000/customer/list/: displays a list of all customers.
- Adicionar: allows you to add a new customer to the database.
- Excluir: allows you to delete an existing customer from the database.
- Buscar: allows you to filter registers by name and last name.

## Credits

This application was created by [Wellington Costa](https://github.com/wellrccity). If you have any questions or suggestions, please feel free to contact me.

## License

[MIT](https://github.com/wellrccity/djangoCRM/blob/master/LICENSE)