import pandas as pd
import FileSystem
from Scrappers.GeneralScrapper import GeneralScrapper
from selenium.webdriver.common.by import By

class Bliga(GeneralScrapper):
    def __init__(self, url):
        print("Bundesliaga init initialized")
        # super().__init__(url)

    def main_loop(self):
        lines = FileSystem.read_text_file("dox5/1920.csv")

        input("XXX")
        print("Send")

        root_elements = self.driver.find_elements(By.CLASS_NAME, "playerRow.container-fluid.linkActive.ng-star-inserted")
        for indx, elem in enumerate(root_elements):
            if indx < 18:
                continue

            try:
                val1 = elem.find_element(By.CLASS_NAME, "first").text
                val2 = elem.find_element(By.CLASS_NAME, "last.font-weight-bold").text
                value = elem.find_element(By.CLASS_NAME, "value.fixed.fixed-large").text
                name = val1 + " " + val2

                for line_indx, line in enumerate(lines):
                    if name in line:
                        lines[line_indx] += "#" + value
            except:
                print("ERR OCCOURED")

        for line_indx, line in enumerate(lines):
            if line.count('#') < 21:
                lines[line_indx] += "#0"

        for line in lines:
            FileSystem.append_string_to_file("dox6/1920.csv", line)


    def double_check(self):
        lines = FileSystem.read_text_file("dox7/2122.csv")
        for line in lines:
            xline = line.strip(',')
            FileSystem.append_string_to_file("dox7/2122_1.csv", xline)




    def csv_to_xls(self):
        test_lines = FileSystem.read_text_file("dox7/2122_1.csv")
        for line in test_lines:
            if line.count(",") != 21:
                print(line)

        csv_file = "dox7/2122_1.csv"
        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        excel_file = "dox8/2122.xlsx"
        try:
            df.to_excel(excel_file, index=False)
            print("CSV file converted to Excel successfully!")
        except Exception as e:
            print(f"Error converting CSV to Excel: {e}")




