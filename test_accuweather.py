from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib, ssl

base_url="https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108"
# declare and initialize driver variable
driver = webdriver.Chrome(executable_path="C:\Auto_Jenkins_Git\WeatherForecast\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(3) 
driver.get(base_url)

date = driver.find_element_by_xpath("//p[@class='date']").text
curentTime = driver.find_element_by_xpath("//p[@class='cur-con-weather-card__subtitle']").text
curentTemp = driver.find_element_by_xpath("//div[@class='cur-con-weather-card__panel']//div[@class='temp']").text
weather = driver.find_element_by_xpath("//span[@class='phrase']").text
airQuality = driver.find_element_by_xpath("//div/span[text()='Air Quality']/following-sibling::span").text
wind = driver.find_element_by_xpath("//div/span[text()='Wind']/following-sibling::span").text
windGuests = driver.find_element_by_xpath("//div/span[text()='Wind Gusts']/following-sibling::span").text
temp = curentTemp.encode('ascii', 'ignore').decode('ascii')


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "dillibabu.aragonda@gmail.com"  # Enter your address
receiver_email = "dillibabu.aragonda@Dell.com"  # Enter receiver address
password = "qmevstitvzxdmwli"

message = """\
Subject: Bangalore Weather forecast from Dilli Python code
To: dillibabu.aragonda@Dell.com

Bengaluru, Karnataka Weather forecast from Accuweather.com. This mail is sent from Python code.\n
Current Date: """ + date + """\n
Current Time: """ + curentTime + """\n
Curent Temp: """ + str(temp) + """ \n
Weather: """ + weather  + """ \n
Wind: """ + wind + """\n
Air Quality: """ + airQuality + """\n
Wind Gusts: """ + windGuests + """

Thanks,
Dilli Babu
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

driver.close()
