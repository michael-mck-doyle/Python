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
'''

# You will need to run the "pip install --upgrade certifi" command in order to get round the "certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>" error
# this example uses reference: https://gist.github.com/Akash-Ansari/e0d868f147c39ecf327215f06b2b27d1


# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://codingnomads.co/"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = str(response.read())

cn_web_output = open('get_html_output_2.txt', 'w')
cn_web_output.write(html)
cn_web_output.close()


# Print the html
#print(html)

# Be polite and close the response!
response.close()
