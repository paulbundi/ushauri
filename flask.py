from flask import Flask, request, redirect, url_for
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
  if request.method == 'POST':
    # Extract form data from request body
    data = request.form

    # Construct email content with HTML format (consider using a templating engine)
    message = MIMEMultipart('alternative')
    message['From'] = 'Appointment Booking System <your_email@example.com>'  # Replace with your email address
    message['To'] = 'paul1bundi@gmail.com'
    message['Subject'] = 'New Appointment Booking'

    html_content = """
    <html>
      <body>
        <h1>Appointment Booking Details</h1>
        <p>Name: {}</p>
        <p>Email: {}</p>
        <p>Phone: {}</p>
        <p>Service: {}</p>
        <p>Counsellor: {}</p>
        <p>Date: {}</p>
        <p>Message: {}</p>
      </body>
    </html>
    """.format(
        data['name'],
        data['email'],
        data['phone'],
        data['service'],  # Assuming 'service' is the name for the counselling selection
        data['counsellor'],
        data['date'],
        data['message']
    )
    part1 = MIMEText(html_content, 'html')
    message.attach(part1)

    # Send email using SMTP (replace with your credentials and server details)
    try:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('your_email@example.com', 'your_password')  # Replace with your email and password
        server.sendmail(message['From'], message['To'], message.as_string())
      print("Appointment details sent successfully!")
      return redirect(url_for('index'))  # Redirect to your index page after successful submission (optional)
    except Exception as e:
      print("Error sending email:", e)
      return "Error submitting appointment. Please try again."  # Return error message

  return "Invalid request method"  # Handle non
