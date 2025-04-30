
### README.md (Setup Summary)
```bash
# Clone repo and setup virtualenv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup env
cp .env.example .env
# Edit .env and add your SMTP credentials

# Run server
python manage.py runserver
```

### requirements.txt (minimal)
Django>=4.2
djangorestframework
django-environ
