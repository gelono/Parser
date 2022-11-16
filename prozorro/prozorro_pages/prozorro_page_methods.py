import time

from selenium.webdriver.common.by import By

from base_tools.base_tools import BaseTools, Driver
from prozorro.prozorro_locators.prozorro_locators import ProzorroLocators


class ProzorroTenders(BaseTools, Driver):
    locators = ProzorroLocators()

    def sort(self):
        """
        Сортировка тендеров на странице по атрибуту "новейшие"
        :return:
        """
        self.element_is_clickable(self.locators.SORT).click()  # click on sort choice
        self.element_is_clickable(self.locators.SORT_NEW).click()  # choice of new tenders sort
        # time.sleep(5)

    def collect_list_of_tenders_from_page(self):
        """
        Сбор веб-ссылок на тендера с одной страницы (20 ссылок по умолчанию)
        :return: list
        """
        try:
            list_of_tenders = self.elements_are_present(self.locators.LIST_TENDERS_PAGE)
        except Exception:
            links = []
            return links
        links = []
        for element in list_of_tenders:
            try:
                link = element.find_element(By.CSS_SELECTOR, 'a[class="search-result-card__title"]').get_attribute('href')
            except Exception:
                link = None
            links.append(link)
        return links

    def collect_total_tender_links(self, max_page=3):
        """
        Сбор всех доступных веб-ссылок для указанного количества страниц - max_page
        :param max_page: int
        :return: list
        """
        total_links = []
        for page in range(1, max_page+1):
            self.loop_driver(f'https://prozorro.gov.ua/search/tender?sort=publication_date,desc&page={page}')
            links = self.collect_list_of_tenders_from_page()
            total_links.extend(links)
        return total_links

    def get_dk_numbers(self, string):
        """
        Парсинг текста в секции "Інформація про предмет закупівлі" на предмет обнаружения номеров тендера.
        :param string: str
        :return: list
        """
        numbers = set()
        while string.find('ДК') != -1:
            index = string.find('ДК')
            new_st = string[index + 2:]
            for symbol in range(len(new_st)):
                if new_st[symbol].isalpha():
                    stop = new_st.find(new_st[symbol])
                    dk = string[index:index + stop + 1]
                    for i in range(-1, -10, -1):
                        if dk[i].isdigit():
                            dk = dk[:len(dk) + i + 1]
                            break
                    break
            string = string[index + stop:]
            dk = dk.replace(' ', '')
            numbers.add(dk)
        return list(numbers)

    def get_status(self):
        """
        Получение "статуса" тендера
        :return: str
        """
        try:
            status = self.element_is_present(self.locators.STATUS)
        except Exception:
            status = 'Немає даних'
        else:
            status = status.text
        return status

    def get_tender_name(self):
        """
        Получение наименования тендера
        :return: str
        """
        try:
            tender_name = self.element_is_present(self.locators.TENDER_NAME)
        except Exception:
            tender_name = 'Немає даних'
        else:
            tender_name = tender_name.text
        return tender_name

    def get_predmet_zakupki(self):
        """
        Сбор информации о предмете закупки
        :return: str
        """
        try:
            predmet_zakupki = self.element_is_present(self.locators.PREDMET_ZAKUPKI)
        except Exception:
            predmet_zakupki = 'Немає даних'
        else:
            predmet_zakupki = predmet_zakupki.text
        return predmet_zakupki

    def get_customer(self):
        """
        Получение наименования Заказчика
        :return: str
        """
        try:
            customer = self.element_is_present(self.locators.CUSTOMER)
        except Exception:
            customer = 'Немає даних'
        else:
            customer = customer.text
        return customer

    def get_customer_edrpu(self):
        """
        Получение ЕДРПУ Заказчика
        :return: str
        """
        try:
            customer_edrpu = self.element_is_present(self.locators.CUSTOMER_EDRPU)
        except Exception:
            customer_edrpu = 'Немає даних'
        else:
            customer_edrpu = customer_edrpu.text
        return customer_edrpu

    def get_initial_price(self):
        """
        Получение первоначальной цены тендера
        :return: float
        """
        try:
            initial_price = self.element_is_present(self.locators.INITIAL_PRICE)
        except Exception:
            initial_price = 'Немає даних'
        else:
            initial_price = initial_price.text
            initial_price = initial_price.replace(' ', '')
            initial_price = float(initial_price[:initial_price.find('U')].replace(',', '.'))
        return initial_price

    def get_finish_price(self):
        """
        Получение окончательной цены тендера
        :return: float
        """
        try:
            finish_price = self.element_is_present(self.locators.FINISH_PRICE)
        except Exception:
            finish_price = 'Немає даних'
        else:
            finish_price = finish_price.text
            finish_price = finish_price.replace(' ', '')
            finish_price = float(finish_price[:finish_price.find('U')].replace(',', '.'))
        return finish_price

    def get_winner(self):
        """
        Получение наименования победителя тендера
        :return: str
        """
        try:
            winner = self.element_is_present(self.locators.WINNER)
        except Exception:
            winner = 'Немає даних'
        else:
            winner = winner.text
            winner = winner[:winner.find('#')-1]
        return winner

    def get_winner_edrpu(self):
        """
        Получение ЕДРПУ победителя тендера
        :return: str
        """
        try:
            winner_edrpu = self.element_is_present(self.locators.WINNER)
        except Exception:
            winner_edrpu = 'Немає даних'
        else:
            winner_edrpu = winner_edrpu.text
            winner_edrpu = winner_edrpu[winner_edrpu.find('#')+1:]
        return winner_edrpu

    def get_list_of_offers(self):
        """
        Получение списка участников тендера
        :return: list
        """
        try:
            list_of_offers = self.elements_are_present(self.locators.LIST_OF_OFFERS)
        except Exception:
            participants = 'Немає даних'
        else:
            participants = [element.text for element in list_of_offers]
        return participants

    def get_start_auction(self):
        """
        Получение даты начала торгов
        :return: str
        """
        try:
            start_auction = self.element_is_present(self.locators.START_AUCTION)
        except Exception:
            start_auction = 'Немає даних'
        else:
            start_auction = start_auction.text
            start_auction = start_auction.replace('Початок аукціону: ', '')
            start_auction = start_auction[:-6]
            start_auction = self.datetime_format(start_auction)
        return start_auction

    def get_publication_date(self):
        """
        Получение даты публикации тендера
        :return: str
        """
        def date_format(date):
            date = date.text
            date = date.replace('Дата оприлюднення: ', '')
            if ':' in date:
                date = date[:-6]
            return date

        try:
            publication_date = self.element_is_present(self.locators.PUBLICATION_DATE_FROM_TABLE)
        except Exception:
            publication_date = 'Немає даних'
        else:
            publication_date = date_format(publication_date)
            publication_date = self.datetime_format(publication_date)

        if publication_date == 'Немає даних':
            try:
                publication_date = self.element_is_present(self.locators.PUBLICATION_DATE)
            except Exception:
                return publication_date
            else:
                publication_date = date_format(publication_date)
                publication_date = self.datetime_format(publication_date)
        return publication_date

    def get_contract_date(self):
        """
        Получение даты заключения договора между победителем и заказчиком
        :return: str
        """
        try:
            contract_date = self.element_is_present(self.locators.CONTRACT_DATE)
        except Exception:
            contract_date = 'Немає даних'
        else:
            contract_date = contract_date.text
            if ':' in contract_date:
                contract_date = contract_date[:-6]
            contract_date = self.datetime_format(contract_date)
        return contract_date