from selenium.webdriver.common.by import By


class ProzorroLocators:
    SORT = (By.CSS_SELECTOR, 'div[class="select"]')
    SORT_NEW = (By.XPATH, '//div[contains(text(),  "            дата публікації – новіші")]')
    LIST_TENDERS_PAGE = (By.CSS_SELECTOR, 'li[class="search-result__item"]')
    LINK_FROM_TENDERS_LIST = By.CSS_SELECTOR, 'a[class="search-result-card__title"]'

    STATUS = (By.XPATH, '//div[@class="tender--head--inf margin-bottom"]/span')
    TENDER_NAME = (By.CSS_SELECTOR, 'div[class="tender--head--title col-sm-9"]')
    PREDMET_ZAKUPKI = (By.CSS_SELECTOR, 'div[class="row margin-bottom"]')
    CUSTOMER = (By.XPATH, '//div[@class="col-sm-9 tender--customer--inner margin-bottom-more"]//table//tr[1]/td[2]')
    CUSTOMER_EDRPU = (By.XPATH, '//div[@class="col-sm-9 tender--customer--inner margin-bottom-more"]//table//tr[2]/td[2]')
    INITIAL_PRICE = (By.CSS_SELECTOR, 'div[class="green tender--description--cost--number"] strong')
    FINISH_PRICE = (By.XPATH, './/h3[contains(text(), "Протокол розкриття")]/parent::div/table/tbody/tr/td[3]')
    WINNER = (By.XPATH, './/h3[contains(text(), "Протокол розкриття")]/parent::div/table/tbody/tr/td[1]')
    LIST_OF_OFFERS = (By.XPATH, './/h3[contains(text(), "Реєстр пропозицій")]/parent::div/table/tbody/tr/td[1]')

    START_AUCTION = (By.XPATH, './/strong[contains(text(), "Початок аукціону:")]/parent::td/parent::tr')
    PUBLICATION_DATE_FROM_TABLE = (By.XPATH, './/strong[contains(text(), "Дата оприлюднення:")]/parent::td/parent::tr')
    PUBLICATION_DATE = (By.XPATH, './/div[contains(text(), "Дата оприлюднення:")]')
    CONTRACT_DATE = (By.XPATH, './/h3[contains(text(), "Укладений договір")]/parent::div//tbody/tr[1]/td[3]')