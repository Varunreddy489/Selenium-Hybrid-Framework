import csv
from datetime import datetime

file_path = "C:\\Users\\varun\\OneDrive\\Desktop\\GE\\WEB AUTOMATION\\orange_hrm\\reports\\test_cases_report.csv"


def create_report(testing_function, test_case, status):
    now = datetime.now()
    curr_time = now.strftime("%Y-%m-%d %H:%M:%S")

    report_row = [
        curr_time,
        testing_function,
        test_case,
        status
    ]
    print("report_row:",
          report_row)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(report_row)

