from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


'''
@paul biernat
'''
def typing(driver):
    url = "https://humanbenchmark.com/tests/typing"
    driver.get(url)
    time.sleep(3)

    text_box = driver.find_element(By.CLASS_NAME, "letters")

    letters = text_box.find_elements(By.TAG_NAME, "span")

    tmp = ""
    for l in letters:
        tmp += l.text
        if (l.text == ""):
            tmp += " "
    
    text_box.send_keys(tmp)
    print(tmp)

    time.sleep(2)

'''
@paul biernat
'''
def reaction_time(driver):
    url = "https://humanbenchmark.com/tests/reactiontime"
    driver.get(url)
    time.sleep(3)

    for i in range(5):
        box = driver.find_element(By.CLASS_NAME, "css-1qvtbrk")

        box.click()

        while True:
            try:
                box = driver.find_element(By.CLASS_NAME, "css-1qvtbrk")
                clicker = box.find_element(By.TAG_NAME, "h1")
            except:
                time.sleep(0.05)
                continue


            box = driver.find_element(By.CLASS_NAME, "css-1qvtbrk")
            clicker = box.find_element(By.TAG_NAME, "h1")

            if (clicker.text == "Click!"):
                clicker.click()
                break

            time.sleep(0.1)

'''
@paul biernat
'''
def aim(driver):
    url = "https://humanbenchmark.com/tests/aim"
    driver.get(url)

    time.sleep(3)

    for i in range(31):
        box = driver.find_elements(By.CLASS_NAME,"css-17nnhwz")
        box[-1].click()


'''
@tyler lammey
'''
def verbal_memory(driver):
    url = "https://humanbenchmark.com/tests/verbal-memory"
    driver.get(url)
    time.sleep(3)
   
    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button')
    #for buttons, find the button in the inspect element > right click > copy > Copy XPath ===> this is what goes into the quotes above
    button.click()
   
    word_set = set()
   
    acc = 0
    while acc<250:
        text_box = driver.find_element(By.CLASS_NAME, "word")
        new_word = text_box.text
               
        if new_word in word_set:
            seen_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]')
            seen_button.click()
        else:
            new_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]')
            new_button.click()
            word_set.add(new_word)
       
        acc += 1
           
'''
@paul biernat
'''
def chimp(driver):
    url = "https://humanbenchmark.com/tests/chimp"
    driver.get(url)

    time.sleep(3)

    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/button')
    button.click()

    ctr = 0
    while ctr < 40:
        grid = []
        all_divs = driver.find_elements(By.CLASS_NAME,"css-19b5rdt")
        all_divs.sort(key=lambda x: int(x.text))

        for div in all_divs:
            print(div.text)
            div.click()

        button = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button')
        button.click()

        ctr += 1

'''
@aashrut jain
@tyler lammey
'''
def number_memory(driver):
    url = "https://humanbenchmark.com/tests/number-memory"
    driver.get(url)
    time.sleep(3)
   
    button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button')
    button.click()
   
    for i in range(30):
        number = driver.find_element(By.CLASS_NAME, 'big-number')
        number = number.text
       
        time.sleep(2+i*0.8)
       
        text_box = text_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')
        text_box.send_keys(number)
       
        submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button')
        submit_button.click()
       
        next_button = driver.find_element(By.CLASS_NAME, 'css-de05nr')
        next_button.click()

categories = {
    "1":["Typing",typing],
    "2":["Reaction Time",reaction_time],
    "3":["Aim",aim],
    "4":["Verbal Memory",verbal_memory],
    "5":["Chimp",chimp],
    "6":["Number Memory",number_memory]
}


while True:
    print("Computer Benchmark")
    print("Choose from the following tests: ")

    for option in categories:
        print(option+". "+categories[option][0])
    
    choice = input(": ")

    if (choice not in categories.keys()):
        print("Invalid option.")
        continue

    driver = webdriver.Chrome()
    categories[choice][1](driver)

    print("Done")
    time.sleep(10)
    break

