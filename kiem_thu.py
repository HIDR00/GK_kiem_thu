
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5173/")
driver.maximize_window()

def check_element_present(id):
    try:
        driver.find_element(By.ID, value=id)
        return True
    except NoSuchElementException:
        return False
    
def register(full_name, phone, email, address, password, confirm_password):
    EC.element_to_be_clickable(driver.find_element(by=By.ID, value="signInAccount").click())
    EC.element_to_be_clickable(driver.find_element(by=By.ID, value="signUpAccount").click())
    driver.find_element(By.ID, "fullName").send_keys(full_name)
    driver.find_element(By.ID, "Phone").send_keys(phone)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "address").send_keys(address)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "ConfirmPassword").send_keys(confirm_password)
    driver.find_element(By.ID, "submitSignUp").click()

    time.sleep(2)
    if check_element_present("submitSignUp"):
        print("Đăng ký thất bại: ")
    else:
        print("Đăng ký thành công: ")
        EC.element_to_be_clickable(driver.find_element(by=By.ID, value="signInAccount").click())



def testRegister():
    # Kiểm thử bỏ trống trường bắt buộc
    register("", "", "test@gmail.com", "Ha Noi", "password123", "password123")

    # Kiểm thử nhập sai định dạng email
    register("Nguyen Van B", "0123456789", "nvb@invalid", "Ha Noi", "password123", "password123")

    # Kiểm thử mật khẩu không khớp
    register("Nguyen Van C", "0123456789", "nvc@gmail.com", "Ha Noi", "password123", "password321")

    # Kiểm thử email đã tồn tại
    register("kevin@gmail.com", "0123456789", "nva@gmail.com", "Ha Noi", "password123", "password123")

    # Kiểm thử đăng ký thành công
    register("Nguyen Van A", "0123456789", "nva1@gmail.com", "Ha Noi", "password123", "password123")



def signIn(email, password):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signInAccount"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submitSignIn"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submitSignIn")))
    if check_element_present("submitSignIn"):
        print("Đăng nhập thất bại: ")
        driver.find_element(by=By.ID, value="email").clear()
        driver.find_element(by=By.ID, value="password").clear()
    else:
        print("Đăng nhập thành công: ")

def testSignIn():

    # Kiểm thử đăng nhập với email không tồn tại
    signIn("nonexistemail@example.com", "123456")

    # Kiểm thử đăng nhập với mật khẩu sai
    signIn("tdt@gmail.com", "wrongpassword")

    # Kiểm thử đăng nhập không nhập email
    signIn("", "123456")

    # Kiểm thử đăng nhập không nhập mật khẩu
    signIn("tdt@gmail.com", "")

    # Kiểm thử đăng nhập với định dạng email sai
    signIn("invalidemail", "123456")

    # Kiểm thử đăng nhập thành công
    signIn("tdt271003@gmail.com", "123456")


def search(keyword):
    driver.execute_script("arguments[0].value = '';", WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ":r1:"))))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ":r1:"))).send_keys(keyword)
    time.sleep(2)

def testSearch():
    search("Tỏi")
    search("Thịt ")
    search("Tảo ")
    search("Sản ")


def testaddCard():
    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'buttonAddToCard'))
    )
    for button in buttons[:3]:
        driver.execute_script("arguments[0]", button)
        button.click()


def testManagementCard():
    testaddCard()
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'shopingCard'))
    )
    button.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'checkAll'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'AddIcon'))
    ).click()
    time.sleep(2)
    minus_icons = driver.find_elements(By.ID, 'minusIcon')
    minus_icons[1].click()

def testFillerItem():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'menuIcon'))
    ).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'fillerItem'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'all'))
    ).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'all'))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'checkAll'))
    ).click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'checkAll'))
    ).click()

# testRegister()
# testSignIn()
# testSearch()
# testManagementCard()
testFillerItem()

