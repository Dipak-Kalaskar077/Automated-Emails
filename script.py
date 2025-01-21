import smtplib  # Built-in library to send emails
from email.mime.multipart import MIMEMultipart  # For email structure
from email.mime.base import MIMEBase  # For attaching files
from email.mime.text import MIMEText  # For email body text (missing import)
from email import encoders  # For encoding attachments
import pandas as pd  # External library for data handling
import os  # For file path handling

# Email credentials
sender_email = "kalaskardipak77@gmail.com"
password = ""  # Use an App Password for security

# List of HR email addresses
hr_emails = [
    "vishalpawar9697@gmail.com",
    "gauravjain@manhuntconsulting.com"
]


# Email content
subject = "Application for a Position that Matches My Skills"
body = """\
Dear Hiring Manager,

I hope this email finds you well.

I am writing to explore potential career opportunities within your esteemed organization. With a strong foundation in Linux administration, AWS Cloud, and containerization tools like Docker, along with hands-on experience in Jenkins and automation, I am confident that my skills can contribute to your team’s success.

Attached, please find my updated resume for your reference. I would welcome the opportunity to discuss how my background and expertise align with your organization's goals.

Thank you for considering my application. I look forward to hearing from you and exploring how I can be a valuable asset to your team.

Best regards,  
Dipak D. Kalaskar  
📞 +91 8830823364  
🔗 linkedin.com/in/dipak-kalaskar 
🔗 github.com/Dipak-Kalaskar077
✉️ er.ddkalaskar@gmail.com  
"""

# Attach resume (Ensure your resume file is in the same directory)
resume_filename = "Dipak Resume DevOps.pdf"
resume_path = os.path.join(os.getcwd(), resume_filename)

# Function to send email with attachment
def send_email(to_email):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach the email body
        personalized_body = body.replace("[Recipient's Name]", to_email.split("@")[0])  # Basic Name Extraction
        msg.attach(MIMEText(personalized_body, "plain"))

        # Attach resume
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={resume_filename}")
            msg.attach(part)

        # Connect to Gmail SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"Email successfully sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Loop through HR emails and send the email
for email in hr_emails:
    send_email(email)
