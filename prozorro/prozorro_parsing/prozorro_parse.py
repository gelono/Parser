from pprint import pprint

from prozorro.prozorro_pages.prozorro_page_methods import ProzorroTenders
from base_tools.base_tools import Driver

new_driver = Driver('https://prozorro.gov.ua/search/tender')
driver = new_driver.driver_setup()
prozorro = ProzorroTenders(driver)

# prozorro.sort()
# prozorro.collect_list_of_tenders_from_page()

total_links = prozorro.collect_total_tender_links(2)
print(len(total_links))
pprint(total_links)

dict_for_database = {}
for link in total_links:
    new_driver = Driver(link)
    driver = new_driver.driver_setup()
    prozorro = ProzorroTenders(driver)

    dict_for_database[link] = {}
    dict_for_database[link]['Веб-посилання'] = link
    dict_for_database[link]['Статус'] = prozorro.get_status()
    dict_for_database[link]['Назва тендеру'] = prozorro.get_tender_name()
    predmet_zakupki = dict_for_database[link]['Предмет закупівлі'] = prozorro.get_predmet_zakupki()
    dict_for_database[link]['Номер тендеру'] = prozorro.get_dk_numbers(predmet_zakupki)
    dict_for_database[link]['Замовник'] = prozorro.get_customer()
    dict_for_database[link]['Замовник_ЄДРПОУ'] = prozorro.get_customer_edrpu()
    dict_for_database[link]['Очікувана ціна'] = prozorro.get_initial_price()
    dict_for_database[link]['Кінцева ціна'] = prozorro.get_finish_price()
    dict_for_database[link]['Переможець'] = prozorro.get_winner()
    dict_for_database[link]['Переможець_ЄДРПОУ'] = prozorro.get_winner_edrpu()
    dict_for_database[link]['Список учасників'] = prozorro.get_list_of_offers()
    dict_for_database[link]['Дата початку аукціону'] = prozorro.get_start_auction()
    dict_for_database[link]['Дата оприлюдення'] = prozorro.get_publication_date()
    dict_for_database[link]['Дата укладення договору'] = prozorro.get_contract_date()

    pprint(dict_for_database[link])

print(dict_for_database)