"""
Patient No-Show Tracker

Analyzes appointment records to identify patients with frequent no-shows
and upcoming appointments within the next 5 days. Outputs a filtered list
to support proactive clinic scheduling and outreach.

Author: Isaac Tsang
"""

import csv
from datetime import datetime, timedelta
import os

CSV_FILENAME = "Patient_NoShow_Tracker_Data.csv"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, CSV_FILENAME)

def upcoming_patients_with_noshow_filter():
    today = datetime.today().date()
    no_show_counts = {}
    patients_with_upcoming = {}

    if not os.path.exists(DATA_FILE):
        print(f"Error: The file '{DATA_FILE}' was not found.")
        print("Make sure the CSV file is in the same folder as this script.")
        return

    # First pass: count past no-shows
    with open(DATA_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            patient_name = row[1].strip()
            status = row[4].strip()
            if status == "No-Show":
                no_show_counts[patient_name] = no_show_counts.get(patient_name, 0) + 1

    # Second pass: find upcoming appointments for patients with 2+ no-shows
    with open(DATA_FILE, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            patient_id = row[0].strip()
            patient_name = row[1].strip()
            appointment_date_str = row[2].strip()
            status = row[4].strip()

            # Only consider patients with 2+ no-shows
            if no_show_counts.get(patient_name, 0) < 2:
                continue

            # Only consider Scheduled appointments
            if status != "Scheduled":
                continue

            try:
                appointment_date = datetime.strptime(appointment_date_str, "%m/%d/%Y").date()
            except ValueError:
                continue

            days_until = appointment_date - today
            if timedelta(days=0) <= days_until <= timedelta(days=5):
                patients_with_upcoming[patient_name] = (patient_id, appointment_date_str)

    # Output results
    if patients_with_upcoming:
        print("Patients with 2+ no-shows and appointments within the next 5 days:")
        for name, (pid, date_str) in patients_with_upcoming.items():
            print(f"{pid}: {name} - Appointment on {date_str}")
    else:
        print("No patients with 2+ no-shows have appointments within the next 5 days.")

if __name__ == "__main__":
    upcoming_patients_with_noshow_filter()
