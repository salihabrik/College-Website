from flask import Flask, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    visitor_email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    email_from = 'N9cJt@example.com'
    email_subject = 'New Form Submission'
    email_body = f"User Name: {name}\nUser Email: {visitor_email}\nSubject: {subject}\nUser Message: {message}\n"
    to = 'N9cJt@example.com'

    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = email_from
    msg['To'] = to
    msg['Reply-To'] = visitor_email

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

    return redirect("contact.html")

if __name__ == '__main__':
    app.run(debug=True)