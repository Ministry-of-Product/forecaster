# main.py


from markupsafe import Markup

from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
import chromedriver_binary  # Adds chromedriver binary to path

chrome_options = Options()

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
#chrome_options = Options()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")



# Initialize a new browser
browser = webdriver.Chrome(options=chrome_options)


@app.route("/")
def hello_world():
    browser.get("https://www.google.com/search?q=headless+horseman&tbm=isch")
    browser.save_screenshot("spooky.png")
    return send_file("spooky.png")
