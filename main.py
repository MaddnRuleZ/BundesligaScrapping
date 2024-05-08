from Scrappers.bligacom import Bliga
from Scrappers.bundesliga import Bundesliga

if __name__ == '__main__':
    db = Bliga("https://www.bundesliga.com/en/bundesliga/stats/players/passes")
    db.csv_to_xls()

