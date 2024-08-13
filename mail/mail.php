<?php

// **Error 1: Sender Email Hardcoded**

// Replace with a variable based on user input or a default sender
$from_email = (isset($_POST['fromEmail'])) ? $_POST['fromEmail'] : 'moneyjarsolutions@gmail.com';

// **Error 2: Missing Method Check**

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('Allow: POST');
    exit;
}

// **Security Improvement: Input Validation and Sanitization**

// Validate and sanitize user input before using it
$name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
$email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
$phone = filter_var($_POST['phone'], FILTER_SANITIZE_STRING);
$subject = filter_var($_POST['subject'], FILTER_SANITIZE_STRING);
$message = filter_var($_POST['message'], FILTER_SANITIZE_STRING);
$subscribed = (isset($_POST['subscribed'])) ? filter_var($_POST['subscribed'], FILTER_SANITIZE_STRING) : 'false';

// **Security Improvement: Environment Variables or Configuration File for Password**

// Consider using environment variables or a configuration file for password
$smtp_server = "smtp.gmail.com";
$smtp_port = 587;

// **Optional: Use PHPMailer Library (More Secure and Feature-Rich)**

// If you need more features or security, consider using a library like PHPMailer

// **Remaining Code:**

$email_message = "

Name: " . $name . "
Email: " . $email . "
Phone: " . $phone . "
Subject: " . $subject . "
Message: " . $message . "
Subscribed to Newsletter: " . $subscribed . "

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
