
## Cara setup di windows
1. Buka folder Project Directory `cd tubespbo`
2. Buat Virtual Environment `python -m venv venv`
3. Activate Virtual Environment `.\venv\Scripts\activate`
4. Install Requirements Package `pip install -r requirements.txt`
5. Migrate Database `python manage.py migrate`
6. Buat Super User `python manage.py createsuperuser`
7. Run The Project `python manage.py runserver`

## Cara setup di linux
1. Buka folder Project Directory `cd tubespbo`
2. Buat Virtual Environment `python -m venv venv`
3. Activate Virtual Environment `source venv/bin/activate`
4. Install Requirements Package `pip install -r requirements.txt`
5. Migrate Database `python manage.py migrate`
6. Buat Super User `python manage.py createsuperuser`
7. Run The Project `python manage.py runserver`