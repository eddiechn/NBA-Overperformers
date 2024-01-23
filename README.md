# Daily NBA Overperformers Report Bot

## Description
This project is an automated bot developed in Python that sends out an email every morning with the NBA's top performers from the previous night. It compares the players' performance against their season averages and highlights significant deviations in an easy-to-read HTML email format.

## Installation


Before running the application, you will need to set up the following environment variables:

EMAIL_SENDER: The email address that will send the reports.
EMAIL_RECEIVER: The email address that will receive the reports.
EMAIL_PASSWORD: The 16-digit app password generated from your Google account's 2-step verification.


For Windows, you can set the environment variables like this in your cmd:
```
set EMAIL_SENDER=your_email@gmail.com
set EMAIL_RECEIVER=receiver_email@gmail.com
set EMAIL_PASSWORD=your_16_digit_code
```
Make sure to replace your_email@gmail.com, receiver_email@gmail.com, and your_16_digit_code with your actual information.

## Usage
To run the bot, execute : 
```
python main.py
```
You will need to set up Windows Task Scheduler to get your daily updates via email.

## Databases
Statistics come from RealGm and CBS Sports
