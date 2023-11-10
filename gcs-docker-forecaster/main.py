# main.py

from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from google.cloud import storage
from datetime import datetime
import requests


URL = 'https://www.google.com/maps/dir/Seattle,+WA/Stevens+Pass,+Washington+98826/@47.7161422,-123.0288051,8z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x5490102c93e83355:0x102565466944d59a!2m2!1d-122.3328481!2d47.6061389!1m5!1m1!1s0x549af0c5541e0005:0xc22c0e63a6ffba92!2m2!1d-121.0859328!2d47.7462223!3e0?entry=ttu'
PATH_TO_CHROMEDRIVER = '/Users/paulin/Documents/GitHub/forecaster/chromedriver/chromedriver'
DIV_NAME = 'Fk3sm fontHeadlineSmall delay-light'
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSf3F8Qc-HYLFXFEQaaodksju73gCSQdOrgni5l4SwxUyPnT0Q/formResponse'
RESULT_FIELD_NAME = 'input.whsOnd.zHQkBf'

# Specify your Google Cloud Storage bucket name and blob name (path to CSV file)
BUCKET_NAME = "p2pforecaster"
BLOB_NAME = "steventime.csv"



def parse_for_minute(time_div):
    # Find the div with the specific class
    print(time_div)
    if time_div:
        time_str = time_div.text.strip()  # "1 hr 34 min"
        hours, minutes = 0, 0

        # Extract hours if present
        if 'hr' in time_str:
            hours = int(time_str.split('hr')[0].strip())

        # Extract minutes if present
        if 'min' in time_str:
            minutes = int(time_str.split('min')[0].split()[-1])

        total_minutes = (hours * 60) + minutes
        print(f"Total time in minutes: {total_minutes}")
        return total_minutes
    else:
        print("Div not found!")

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

app = Flask(__name__)

@app.route("/")
def getDriveTime():
    # Initialize a new browser
    driver = webdriver.Chrome(options=chrome_options)

    # Let's give it some time to render and execute JavaScript
    driver.implicitly_wait(10)

    # Navigate to the URL
    driver.get(URL)

    # Get the rendered HTML source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Locate the desired div
    time_div = soup.find('div', class_=DIV_NAME)
    print(time_div)
    minutes = parse_for_minute(time_div)

    # Close the browser
    driver.quit()

    # Convert minutes to a string before sending as a response
    response = f"Total minutes: {minutes}"

    # Append the results onto a csv file
    now = datetime.now() #current date and time
    formatted_date_time = now.strftime("%Y-%m-%dT%H:%M:%S")
    new_line = f"{formatted_date_time},{minutes}"
    # Call the function to append the line to the CSV
    append_line_to_csv(BUCKET_NAME, BLOB_NAME, new_line)


    return response

def append_line_to_csv(bucket_name, blob_name, new_line):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Download the existing CSV file if it exists
    try:
        existing_data = blob.download_as_text()
    except Exception as e:
        existing_data = ""

    # Append the new line to the existing data
    updated_data = existing_data + new_line + "\n"

    # Upload the updated data back to the blob
    blob.upload_from_string(updated_data)

if __name__ == "__main__":
    app.run()
