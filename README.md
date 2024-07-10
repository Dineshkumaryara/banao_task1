# Banao Technologies Tasks

This repository contains a Django project completed as part of a task for Banao Technologies.

## Project Overview

This project includes the following key features:

1. **User Authentication**: A custom user model with separate roles for patients and doctors, using Django's built-in authentication system.
2. **Admin Panel Customization**: Customized admin interfaces for managing patient and doctor information.
3. **Basic Frontend**: A simple login form with a back button, styled using CSS.
4. **Blog System**: Doctors can create, edit, and manage blog posts. Patients can view blog posts categorized by Mental Health, Heart Disease, Covid19, and Immunization.

## Steps Completed

### Setting Up the Project

- Created a new Django project and app.
- Configured settings and created initial models for users (patients and doctors).

### Implementing User Authentication

- Created a custom user model.
- Implemented user registration and login views.
- Customized the admin panel to handle the custom user model.

### Frontend Development

- Designed a login form with a back button that redirects to the home page.
- Ensured the login and back buttons are displayed side by side using CSS.

### Blog System

- Added a blog post model with fields for title, image, category, summary, content, and draft status.
- Implemented views and templates for creating, editing, and viewing blog posts.
- Integrated the blog functionality into the doctor and patient dashboards.
- Styled the blog section for a better user experience, including smooth transitions and hover effects on images.

### Deployment

- Deployed the project on PythonAnywhere.
- Configured static files handling for the admin interface.

