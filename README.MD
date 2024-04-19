# Trellis Law

## Overview

This repository hosts a full-stack application designed to convert numeric values into their corresponding English word representation. The back-end is built using Django, exposing two primary API endpoints that allow users to input numbers and receive them as written words. The front-end is a Vue/Nuxt application that provides a user-friendly interface for real-time interaction with the API. The project also includes infrastructure-as-code for AWS deployment using AWS Cloud Development Kit (CDK).

### Components

- **API backend:** A Django application with endpoints to convert numbers into words.
- **Frontend:** A Vue/Nuxt application that interacts with the Django API.
- **Infrastructure:** CDK scripts for deploying the application on AWS.

### Project Structure

- `/backend`: Contains the Django application with all necessary configurations for the API backend. Please refer to the `README.md` in this folder for detailed information on setup, usage, and API documentation.
- `/ui`: Houses the Vue/Nuxt application code. The `README.md` in this folder provides instructions on installation, running the app locally, and building for production.
- `/infra`: Includes the CDK deployment scripts for setting up AWS infrastructure. Check the `README.md` here for details on deploying the application to AWS.

## Getting Started

To begin using this project, follow these steps:

1. **Clone the Repository:**

   ```
   git clone git@github.com:lguibr/trellis-law.git
   cd trellis-law
   ```

2. **API Server Setup:**
   Navigate to the `/backend` directory and follow the instructions in the `README.md` to set up the Django server.

3. **Frontend Setup:**
   Move to the `/ui` folder and follow the setup instructions detailed in the `README.md` to get the frontend running.

4. **Infrastructure Setup:**
   Enter the `/infra` directory and follow the deployment instructions in the `README.md` to deploy the application using AWS CDK.

## High-Level Functionality

- **Convert Numbers to Words:**

  - **GET `/num_to_english?number=<number>`:** Returns the English word representation of the provided number.
  - **POST `/num_to_english`:** Accepts a JSON object with a "number" key and returns the English word representation.

- **Frontend Interaction:**
  - The landing page allows users to input a number and displays the English words immediately on path /number=<number> and after a 5-second delay with a loading spinner when accessing root and filling a number.

## Requirements

- Python 3.11
- Django 5.X
- Vue.js 3.x/Nuxt.js 2.x
- AWS Account for deploying with CDK
- Node.js 20.x+ for frontend development

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
