'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!
'''
'''
___References___

Performing HTTP requests in Python using urllib - https://gist.github.com/Akash-Ansari/e0d868f147c39ecf327215f06b2b27d1
Python Urllib Module - Urllib module is the URL handling module for python. - https://www.geeksforgeeks.org/python-urllib-module/
[SSL: CERTIFICATE_VERIFY_FAILED] - Answered here: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org#50243316
Web Scraping Python Tutorial for Beginners - https://intellipaat.com/blog/tutorial/python-tutorial/python-web-scraping-tutorial/
Using BeautifulSoup to parse HTML and extract press briefings URLs - http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/#extracting-text-from-soup
'''

# This example uses reference https://intellipaat.com/blog/tutorial/python-tutorial/python-web-scraping-tutorial/
# You will need to run the "pip install --upgrade certifi" command in order to get round the "certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>" error
#Step 1: Fetch the web page and convert the html page into text with the help of Python request library
#import the python request library to query a website
# Import packages

import requests

# #specify the url we want to scrape from

cn_html_output = requests.get('https://codingnomads.co/').text

#convert the web page to text and print it

#print(cn_html_output)


# how to convert the web page data to a text file?

cn_web_output = open('get_html_output_1.txt', 'w')
cn_web_output.write(cn_html_output)
cn_web_output.close()
