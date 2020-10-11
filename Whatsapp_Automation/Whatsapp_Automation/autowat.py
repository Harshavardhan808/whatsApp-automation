import pandas as pd
import time
from selenium import webdriver
from progress.bar import Bar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def upload_csv():
    try:
        csv = input("Enter the path of the csv file: ")
        header = ["Name", "Affiliate_ID", "Phone", "Parent_ID"]
        global df
        df = pd.read_csv(csv, names=header)
        df.dropna(axis=0, inplace=True)
        bar = Bar('Processing .csv file', max=100)
        for i in range(100):
            time.sleep(0.02)
            bar.next()
        print("\nCSV added successfully!!!")
    except:
        print("Fail to load the csv file. Kindly check the file path.")
        exit()


def send_msg():
    count=0
    for i,j in zip(df["Phone"], df["Affiliate_ID"]):
        if i.isalnum()==True:
            try:
                number = "91{}".format(i)
                extension = "?ref={}&t=l".format(j)
                link = inp + extension
                message = 'Thank you for being a part of eMoment.in family!! Check out our new product {} Have a great day!'.format(link)
                url = 'https://wa.me/{}'.format(number)
                driver.get(url)
                continue_to_chat = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/a").click()
                time.sleep(1)
                whatsapp_web = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/a").click()
                time.sleep(2)
                click_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_3uMse')))
                time.sleep(10)
                toext_box = driver.find_element_by_class_name("_3uMse").send_keys(message)
                send_button = driver.find_element_by_class_name("_1U1xa").send_keys(Keys.ENTER)
                time.sleep(2)
                count += 1
                if count % 10 == 0:
                    time.sleep(15)
                else:
                    pass
            except:
                print('Message cannot be send to the number {} as this number is not available on Whatsapp.'.format(i))
        else:
            print("The number {} with affiliate ID {} is invalid".format(i,j))


if __name__ == '__main__':
    print("\n")
    print("****************************** Welcome to the Whatsapp Automation Software ******************************")
    print("\n")
    upload_csv()

    inp = input("Enter the link: ")
    options = webdriver.ChromeOptions()
    CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\harshavardhan\\PycharmProjects\\Whatsapp_Automation\\Everything"
    options.add_argument(CHROME_PROFILE_PATH)

    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.maximize_window()

    send_msg()

    print("\n")
    print("************************ Thank you for using the Whatsapp Automation Software ************************")
    driver.close()
    exit()