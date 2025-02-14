# Electronics-shopping-store
  

# Project Title

Zencart

## Installation

To install and set up the project on your local machine, follow these steps:
**Clone the repository**:
   ```bash
   git clone https://github.com/surya4032/Electronics-shopping-store
   ```

## Navigate to the project directory:

```bash
cd <project-directory>
```

Set up a virtual environment:
For Linux/Mac:
```bash
python3 -m venv virt
```
For Windows:
```bash
python -m venv virt
```

## Activate the virtual environment:

For Linux/Mac:
```bash
source virt/bin/activate
```
For Windows:
```bash
virt\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

# Project Setup

## Environment Variables

To run this project, you will need to set up the following environment variables in a `.env` file at the root of the project.

### Example `.env` file

```
SECRET_KEY=your_secret_key
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
EMAIL_HOST_USER=your_email@example.com  # Website email address
EMAIL_HOST_PASSWORD=your_email_password  # Email password
```

### Steps to Obtain Environment Variables

1. **Contact the Admin**: Reach out to the project admin or your team lead to get access to the required environment variables.
2. **Secure Storage**: The environment variables will be shared with you through a secure communication channel or stored in a secure environment management tool.
3. **Setup**: Once you have the environment variables, create a `.env` file at the root of the project and add the variables to it.

# Usage
To use the project, follow these steps:

Activate the virtual environment (if not already activated).

Run the project:
*check whether you are in the project directory
```bash
run the following command 'cd mysite' in the terminal
```
## To start the Django server,
```bash
run 'python manage.py' runserver command in the terminal
```

# Contribution
We welcome contributions! If you’d like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Make your changes.
Commit and push your changes.
Create a pull request with a clear description of what you’ve done.

---






