from flask import Flask, render_template, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        # Assuming the select element for counselling has id="counselling"
        counselling = request.form.get('counselling')  # Use get in case it's not selected
        # Assuming the select element for counsellor has id="counsellor"
        counsellor = request.form.get('counsellor')  # Use get in case it's not selected
        date = request.form['date']
        message = request.form['message']

        # Prepare email content
        email_body = f"""
        Appointment Request - {name}

        Name: {name}
        Email: {email}
        Phone: {phone}
        Counselling: {counselling}
        Counsellor: {counsellor}
        Date: {date}
        Message: {message}
        """

        # Configure email sending (replace with your details)
        sender_email = "moneyjarsolutions@gmail.com"
        sender_password = "oxrflckpjennxxiw"
        receiver_email = "paul1bundi@gmail.com"

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = f"Appointment Request - {name}"
        message.attach(MIMEText(email_body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com',  587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            return f"Thank you, {name}! Your appointment request has been submitted. We will confirm by Text Message."
        except Exception as e:
            print(f"Error sending email: {e}")
            return "There was an error submitting your appointment request. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)
