from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import threading

app = Flask(__name__)

# ======================
# EMAIL CONFIG (HARDCODED)
# ======================
EMAIL_ADDRESS = "bitgetwalletorg@gmail.com"
EMAIL_PASSWORD = "fsjifnpevjevdzcs"  # Gmail App Password

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ======================
# RECIPIENTS
# ======================
recipients = [
    "ringpon123@gmail.com",
    "s1.h.s@hotmail.com",
    "itamar203.ia@gmail.com",
    "iVasile.09vasile.02@gmail.com",
    "SavaCerasela1@gmail.com",
    "Krisztinamali4@gmail.com",
    "Iuliana8899@gmail.com",
    "anaticiuc.ion2210@gmail.com",
    "bandi050633@gmail.com",
    "noncsy725@gmail.com",
    "tolnail593@gmail.com",
    "napsugarvirag299@gmail.com",
    "mariann680924@gmail.com",
    "szurokakatalin29@gmail.com",
    "danielzabari01@gmail.com",
    "tpetoerzsebet95@gmail.com",
    "laczkoaron@gmail.com",
]

# ======================
# LOAD HTML TEMPLATE
# ======================
with open("email_template.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# ======================
# SEND EMAIL FUNCTION
# ======================
def send_email():
    for recipient in recipients:
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = "Daily Announcement"
        msg.attach(MIMEText(html_content, "html"))

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
            server.quit()
            print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")

# ======================
# SCHEDULER
# ======================
def schedule_emails():
    schedule.clear()

    schedule.every().day.at("10:00").do(send_email)
    schedule.every().day.at("2:05").do(send_email)
    schedule.every().day.at("9:07").do(send_email)

    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

# ======================
# START SCHEDULER ONCE
# ======================
scheduler_thread = threading.Thread(target=schedule_emails)
scheduler_thread.daemon = True
scheduler_thread.start()

# ======================
# ROUTE
# ======================
@app.route("/")
def home():
    return "<h1>Email Scheduler is running!</h1>"

# ======================
# RUN FLASK
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
