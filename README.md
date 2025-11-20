# Full-Stack Car Dealership Application

## Project Overview
This project is a full-stack web application for managing car dealerships and customer reviews. It is built with **Django** for the backend and **React** for the frontend. The application also integrates a sentiment analysis microservice deployed on IBM Cloud Code Engine.  

## Users can:
- Browse car makes and models.
- View dealership details and reviews.
- Post reviews with sentiment analysis.
- Register and log in with authentication.  

## Features
- **Django Backend**
  - REST API endpoints for dealers, reviews, and cars.
  - SQLite database with CarMake and CarModel tables.
  - Admin panel to manage cars, models, and users.
  
- **React Frontend**
  - Dealer listing page.
  - Dealer detail and review page.
  - Login and registration functionality.
  
- **Microservices**
  - Sentiment analysis service deployed on Code Engine.
  
- **Containerization & Kubernetes**
  - Dockerized Django backend.
  - Kubernetes deployment YAML for cluster deployment.
  - Port forwarding to access the running application.

## Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd xrwvm-fullstack_developer_capstone/server
```
2. Backend setup
```bash
# Create a virtual environment
python3 -m venv djangoenv
source djangoenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Build frontend
cd ../frontend
npm install
npm run build
```

3. Run Django server
```bash
cd ../server
python manage.py runserver
```

# Microservices

Ensure the sentiment analysis microservice is deployed and running.

Update ```.env``` with the deployment URL:

```
sentiment_analyzer_url=<DEPLOYED_MICROSERVICE_URL>
```

# Access the application

Frontend: http://localhost:8000

Admin panel: http://localhost:8000/admin

Superuser credentials: root / root

Docker & Kubernetes

Build Docker image:

```bash
docker build -t us.icr.io/<your-namespace>/dealership .
docker push us.icr.io/<your-namespace>/dealership
```

Deploy using Kubernetes:

```bash
kubectl apply -f deployment.yaml
kubectl port-forward deployment.apps/dealership 8000:8000
```

Access deployed app: ```<DEPLOYED_KUBERNETES_URL>```


# Technologies Used

Python, Django, Django REST Framework

React, JavaScript, HTML, CSS

Docker, Kubernetes, IBM Cloud Code Engine

SQLite, NLTK (sentiment analysis)

# Author
## Umme Sanjeda


Deployed Application URL:
```(https://ummesanjedaw-8000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/)```

