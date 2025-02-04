# Multilang - FAQ :globe_with_meridians: :sparkles: 
- Welcome to the Multilang FAQ System repository! This project is designed to manage frequently asked questions (FAQs) with multi-language support using Django. It ensures efficient storage, retrieval, and translation of FAQs while following best development practices.
---

## Key Features :star2:

- **Multi-language FAQ Management**: 
  Supports translations in multiple languages (e.g., English, Hindi, Bengali). Dynamic retrieval of translations based on user preference.
  
- **WYSIWYG Editor Integration**: 
 Rich-text formatting enabled for answers using django-ckeditor. Seamless multilingual content support.
  
- **RESTful API with Language Support**:
  Query parameter ?lang= to fetch FAQs in different languages. Optimized pre-translation for better response time.
  
- **Caching Mechanism**: 
  Implements Django cache framework with Redis for improved performance.

- **Automated Translations**: 
Uses Google Translate API (googletrans) for automatic translation. Fallback to English if a translation is unavailable.

- **Admin Panel**: 
 User-friendly Django admin interface for managing FAQs.
---

## Tech Stack :computer: 
 
- **Backend**: Python, Django, Django REST Framework (DRF)
- **Database**:  SQLite
- **Caching**: Redis
- **Translation API**: Google Translate (googletrans)
- **Infrastructure**: Docker, AWS

---

## Getting Started

Follow the steps below to set up the Multilang FAQ System:

## 1 . **Clone the Repository:** 
Clone this repository to your local machine using the following command: 
 
  
  ```
 git clone https://github.com/Ashish8329/multilang-faq.git
``` 
## 2 . Set Up a Virtual Environment
> [!IMPORTANT]
> Before proceeding, it's recommended to set up a Python virtual environment for the project.
```
 python3 -m venv venv
```
> [!IMPORTANT]
> Activate Virtual env 
```
source venv/bin/activate
```
> [!IMPORTANT]
> Install Dependencies
```
 pip install -r requirements.txt
```

## 3.  Navigate to Project Directory: 
Go to the directory where you cloned the repository.
```
 cd lingo_faq
```
 
## 4. Create Superuser: 
After the project is successfully set up, create a superuser using the following command:
```
python3 manage.py createsuperuser 
```
Follow the prompts to set up the superuser credentials. 

 
## 4. Run celery with flower: 
After the project is successfully set up, run the celery using the following command:
```
celery -A lingo_faq flower --detach
```

## 5. Run celery with log for debug: 
Run the celery debug using the following command:
```
celery -A lingo_faq worker --loglevel=debug
```
 

## 6. Run the Development Server: 
After the project is successfully set up, create a superuser using the following command:
```
python manage.py runserver
```
Now visit http://127.0.0.1:8000/admin/ to manage FAQs.
For Flawer visit http://localhost:5555/workers.

---

## Contribution Guidelines
We welcome contributions! Please follow these steps:
> Fork the repository.
> Create a feature branch (feat/multilang-support).
> Commit with clear messages (e.g., feat: Add multilingual FAQ model).
> Push changes and create a pull request.


## 8. Explore the Multilang system: :sparkles:'
:point_right: **Congratulations**:balloon:!:tada::tada: Your Multilang system is now ready to explore.:confetti_ball:	:balloon: :point_left:
