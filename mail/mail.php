<?php

// Replace with your actual SMTP server details
$smtp_server = "smtp.gmail.com";
$smtp_port = 587;

// Consider using environment variables or a configuration file for password
$smtp_username = "moneyjarsolutions@gmail.com";
$smtp_password = "oxrflckpjennxxiw";

$from_email = $_POST['moneyjarsolutions@gmail.com']; // Sender's email address from JavaScript
$to_email = "paul1bundi@gmail.com"; // Recipient's email address

$name = $_POST['name'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$subject = $_POST['subject'];
$message = $_POST['message'];
$subscribed = $_POST['subscribed'];

$email_message = "

Name: " . $name . "
Email: " . $email . "
Phone: " . $phone . "
Subject: " . $subject . "
Message: " . $message . "
Subscribed to Newsletter

";

$headers = 'From: ' . $from_email . "\r\n" .
    'Reply-To: ' . $email . "\r\n" .
    'Content-Type: text/plain; charset=UTF-8' . "\r\n";

if (mail($to_email, $subject, $email_message, $headers)) {
    echo 'Email sent successfully!';
} else {
    echo 'There was an error sending the email.';
}

?>