# Mingle - Django Chat Application - Deployment Guide

This guide explains how to deploy a Django-based chat application on an AWS EC2 instance using Nginx.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup & Configuration](#setup--configuration)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you start, ensure you have the following:
- AWS EC2 instance with Ubuntu or a similar Linux distribution.
- SSH access to your EC2 instance.
- Python 3.x, `virtualenv`, `pip` installed.
- Nginx installed (for production server setup).
- Gunicorn installed (to serve the Django app).

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/Vaishnav88sk/MingleChat-django-web.git
cd MingleChat-django-web
```
2. **Create a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```
4. **Setup Database:**
```bash
python manage.py migrate
```

## Setup & Configuration

1. **Create a Superuser:**
```bash
python manage.py createsuperuser
```
2. **Update Settings for Production:**
```bash
ALLOWED_HOSTS = ['your-ec2-public-ip', 'your-domain.com','localhost']
```
3. **Collect Static Files:**
```bash
python manage.py collectstatic
```

## Running the Application

```bash
python manage.py runserver 0.0.0.0:8000
```

## Troubleshooting

1. **Django Static Files:**
```bash
python manage.py collectstatic
```

2. **Database Issues:**
```bash
python manage.py migrate
```

**Visit the website: https://minglechat.duckdns.org**
