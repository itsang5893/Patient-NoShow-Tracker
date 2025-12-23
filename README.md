Patient No-Show Tracker

A Python-based tool that analyzes patient appointment records to identify individuals with frequent no-shows and upcoming appointments within the next 5 days. Generates a concise report to support proactive clinic scheduling and outreach.

Author: Isaac Tsang

Project Overview

This project demonstrates the ability to work with Python, CSV data, and date logic to support data-driven decision-making in healthcare. It highlights skills in:

Data parsing and aggregation with Python dictionaries

Filtering based on multiple conditions (no-show count and upcoming appointments)

Date calculations using the datetime module

Clean, formatted console output

Getting Started: 

Ensure the CSV file Patient_NoShow_Tracker_Data.csv is in the same folder as the script.

Run the Python script:

python Patient_NoShow_Tracker.py


The program will output a list of patients with 2+ past no-shows who have scheduled appointments within the next 5 days.

Example Output: 
Patients with 2+ no-shows and appointments within the next 5 days:

P001: John Doe - Appointment on 12/24/2025 

P002: Jane Smith - Appointment on 12/25/2025 

P003: Emily Brown - Appointment on 12/23/2025 


Dependencies: 

Python 3.x

Built-in libraries only (csv, datetime, os)

Notes: 

Appointment dates in the CSV must be formatted as MM/DD/YYYY.

Designed for demonstration and testing purposes using sample data.
