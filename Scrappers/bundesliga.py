import random
import time
from selenium.webdriver.common.by import By

import FileSystem
from Scrappers.GeneralScrapper import GeneralScrapper

class Bundesliga(GeneralScrapper):
    def __init__(self, url):
        print("Bundesliaga init initialized")
        super().__init__(url)


    def main_loop(self):
        input("CHECK NAVIGATION")

        body = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[6]/div[3]/div[4]/table/tbody")
        rows = body.find_elements(By.TAG_NAME, "tr")
        print(str(len(rows)))
        for row in rows:
            csv = self.extract_row(row)
            if not csv:
                continue

            FileSystem.append_string_to_file("Bundesliga_1920.txt", csv)

    def extract_row(self, row):
        rank = self.by_name(row, "right ")
        if not rank:
            return None

        name = self.by_name(row, "left ")
        nationality_text = self.driver.find_element(By.XPATH, '//td[@class="left poptip" and @data-stat="nationality"]/a').text
        pos = self.by_name(row, "center ")
        team_element = row.find_element(By.XPATH, '//td[@class="left " and @data-stat="team"]').text
        age = row.find_element(By.XPATH, '//td[@class="center "][@data-stat="age"]').text
        born = row.find_element(By.XPATH, '//td[@class="center "][@data-stat="birth_year"]').text

        mp = row.find_element(By.XPATH, './/td[contains(@class, "right") and contains(@class, "group_start")][@data-stat="games"]').text
        starts = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="games_starts"]').text
        min = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="minutes"]').text
        ninty = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="minutes_90s"]').text
        goals = row.find_element(By.XPATH, './/td[contains(@class, "right") and @data-stat="goals"]').text
        assists = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="assists"]').text
        goals_assists = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="goals_assists"]').text
        pens_made = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="pens_made"]').text
        pens_att = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="pens_att"]').text
        cards_yellow = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="cards_yellow"]').text
        cards_red = row.find_element(By.XPATH, './/td[contains(@class, "right")][@data-stat="cards_red"]').text

        # Concatenate all data into a CSV string
        csv_string = f"{rank}#{name}#{nationality_text}#{pos}#{team_element}#{age}#{born}#{mp}#{starts}#{min}#{ninty}#{goals}#{assists}#" \
                     f"{goals_assists}#{pens_made}#{pens_att}#{cards_yellow}#{cards_red}"

        return csv_string

        # print(rank)

    def by_name(self, row, name):
        try:
            return row.find_element(By.CLASS_NAME, name).text
        except:
            return None
            print("ERROR")

    def by_xpath(self, row, xpath):
        try:
            return row.find_element(By.CLASS_NAME, xpath).text
        except:
            print("ERROR")


