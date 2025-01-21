# Automated-Emails

This project automates the process of sending emails using a Python script.

## Prerequisites

Before you begin, ensure that you have the following installed on your system:

1. **Python**: 
   Download and install Python from [here](https://www.python.org/downloads/).

2. **Pandas**:
   Install the `pandas` library using the following command:
   ```bash
   pip install pandas


## Libraries Used

* smtplib: Used to send emails through SMTP servers like Gmail, Yahoo, etc.
email.mime.multipart: Used to create the email structure (sender, receiver, subject, etc.).
email.mime.base and email.encoders: Used for adding attachments (like your resume).
pandas: Used if you want to manipulate or manage data, such as the list of HR emails (if stored in a file).

## Steps Followed to Execute the Script
Below are the detailed steps followed to execute the script:

1. Install Required Python Libraries
First, we install the required libraries using pip. The libraries needed for the script are pandas, smtplib, and email. Use the following command in your terminal:

''pip install pandas smtplib email ''

smtplib is part of the Python standard library, so no installation is needed for that.
pandas is used for handling data (such as HR email lists stored in a CSV file).

2. Create Gmail App Password
We use an App Password instead of a regular Gmail password for security purposes.
Go to your Google Account settings and create an app password.
Make sure 2-Step Verification is enabled for your account. Then, under the "Security" section, generate an app password specifically for the Python email automation script.

3. Set Up the Script with Your Credentials
In the Python script, you'll need to input your Gmail email address and the generated App Password:

python
Copy
Edit
sender_email = "kalaskardipak77@gmail.com"
password = "your_app_password_here"
Replace your_app_password_here with the App Password generated in Step 2.

4. List of HR Emails
You can add the list of HR email addresses in the hr_emails list:

python
Copy
Edit
hr_emails = [
    "hr1@example.com",
    "hr2@example.com",
    ...
]

5. Customize the email body

6. Run the Script
Once everything is set up, run the script using the following command:
``
python send_emails.py
``