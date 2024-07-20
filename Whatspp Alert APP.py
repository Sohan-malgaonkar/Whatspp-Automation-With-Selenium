from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import xlwings as xw
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
options= webdriver.ChromeOptions()
#chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
chrome_options.add_argument("user-data-dir=C:\\Users\\Replace Username\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://web.whatsapp.com/")
# time.sleep(5)

wb = xw.Book('ContMsg.xlsx')
sheet = home_sheet = wb.sheets['Sheet1']

last_row = sheet.range('A' + str(sheet.cells.last_cell.row)).end('up').row
mbl = []
for row in range(2, last_row + 1):
    data = sheet.range(f'A{row}').value
    #print(data)
    if data is not None:
        mobile_no = str(data).rstrip('.0')
        mbl.append(mobile_no)
print("Mobile numbers list:", mbl)

finalcontact=mbl

# print("final mobile no list",finalcontact)
# for i in finalcontact:
#     print("Mobile no is",i)
    
# Specify the name of your Notepad file
file_name = 'Client_Message.txt'

# Open the file in read mode
with open(file_name, 'r') as file:
    # Read the contents of the file
    My_message = file.read()

# Print the contents to the console
print(My_message)
for i in finalcontact:
    print("this is one by one number:", i)

    driver.get(f"https://web.whatsapp.com/send?phone={i}&text={My_message}")
    driver.maximize_window()
    time.sleep(6)

    el = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
#                                      //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button
#                                      //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]                                                      
    el.send_keys(Keys.ENTER)
    time.sleep(2)
    
# print("All messages sent!")
input()