from pprint import pprint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from prozorro.prozorro_pages.prozorro_page_methods import ProzorroTenders

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://prozorro.gov.ua/tender/UA-2022-11-15-005461-a')

# e = driver.find_element(By.XPATH, './/h3[contains(text(), "Укладений договір")]/parent::div//tbody/tr[1]/td[3]')
# print(e.text)
prozorro = ProzorroTenders(driver)
table_field = prozorro.get_contract_date()
pprint(table_field)


# e = e.text
# e = e.replace(' ', '')
# e = float(e[:e.find('U')].replace(',', '.'))
# pprint(e)

# st = "Вид предмету закупівлі: Товари Класифікатор та його відповідний код: ДК 021:2015:39220000-0: " \
#      "Кухонне приладдя, товари для дому та господарства і приладдя для закладів громадського харчування  " \
#      'Опис окремої частини або частин предмета закупівлі 2 штуки Кисть '"стандарт"' 1д Місце поставки товарів або місце' \
#      ' виконання робіт чи надання послуг: 54029, Україна, Миколаївська область, м. Миколаїв, Рюміна, 5 Строк поставки ' \
#      'товарів, виконання робіт чи надання послуг: 31 грудня 2022 ДК 021:2015: 39220000-0 — Кухонне приладдя, товари ' \
#      'для дому та господарства і приладдя для закладів громадського харчування 2 штуки Кисть '"стандарт"" 1,5д Місце " \
#      "поставки товарів або місце виконання робіт чи надання послуг: 54029, Україна, Миколаївська область, м. Миколаїв, " \
#      "Рюміна, 5 Строк поставки товарів, виконання робіт чи надання послуг: 31 грудня 2022 ДК 021:2015: 39220000-0 — " \
#      "Кухонне приладдя, товари для дому та господарства і приладдя для закладів громадського харчування"
#
#
# def get_dk_numbers(string):
#     numbers = set()
#     while string.find('ДК') != -1:
#         index = string.find('ДК')
#         new_st = string[index + 2:]
#         for symbol in range(len(new_st)):
#             if new_st[symbol].isalpha():
#                 stop = new_st.find(new_st[symbol])
#                 dk = string[index:index + stop + 1]
#                 for i in range(-1, -10, -1):
#                     if dk[i].isdigit():
#                         dk = dk[:len(dk) + i + 1]
#                         break
#                 break
#         string = string[index + stop:]
#         dk = dk.replace(' ', '')
#         numbers.add(dk)
#     return list(numbers)
#
# numbers = get_dk_numbers(st)
# print(numbers)
