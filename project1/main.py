import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os

# thoughts -- https://www.w3schools.com/python/python_dictionaries.asp

# Load the searches.json file from the searches-db folder
# json_file_path = os.path.join(os.path.dirname(__file__), 'searches-db', 'searches.json')
# with open(json_file_path, 'r') as file:
#     data = json.load(file)

# Example usage of the loaded JSON data
# for university in data['universities']:
#     print("uni_id", university['uni_id'])
#     print(" ")
#     print("uni_name", university['uni_name'])


# will place into seperate file later on
# bill microsoft has caught onto the universities being searched repeatedly now it doesn't generate points
searchesUni = [
    "University of Aberdeen",
    "University of Edinburgh",
    "University of Glasgow",
    "University of St Andrews",
    "University of Stirling",
    "University of Strathclyde",
    "University of Dundee",
    "University of Abertay Dundee",
    "University of the Highlands and Islands",
    "University of the West of Scotland",
    "University of the West of England",
    "University of the Arts London",
    "University of the Creative Arts",
    "University of the London", #???
    "University of Central Lancashire",
    "University of East Anglia",
    "University of East London",
    "University of Essex",
    "University of Exeter",
    "University of Kent",
    "University of Leicester",
    "University of Lincoln",
    "University of Liverpool",
    "University of London",
    "University of Manchester",
    "University of Newcastle",
    "University of Northampton",
    "University of Nottingham",
    "University of Oxford",
    "University of Plymouth",
    "University of Portsmouth",
    "University of Reading",
    "University of Salford",
    "University of Sheffield",
    "University of Southampton",
    "University of Sunderland",
    "University of Surrey",
    "University of Sussex",
    "University of Warwick",
    "University of West London",
    "University of Westminster",
    "University of Wolverhampton",
    "University of Worcester",
    "University of York",
    "University of Aberdeen"
]

gamesSearches = [
    "ELDEN RING",
    "Halo Infinite",
    "Horizon Forbidden West",
    "God of War Ragnarok",
    "Starfield",
    "The Legend of Zelda: Breath of the Wild 2",
    "Final Fantasy XVI",
    "Fable",
    "The Elder Scrolls VI",
    "Metroid Prime 4",
    "Silent Hill",
    "Age of Empires II",
    "Bloons Tower Defense 6",
    "Bloodborne",
    "Call of Duty: Warzone",
    "Cuphead",
    "Dark Souls III",
    "Dead by Daylight",
    "Dead Space",
    "Death Stranding",
    "Demon's Souls"
]

# same with this one
RewardsPageElements = [
    "Bing Homepage Quiz",
    "30 points >",
    "10 points>",
    "5 points >",
    "Learn the facts",
    "Explore now",
    "Search now",
    "Check the latest forcast"
]

# ------------------------------------------------ testing a for loop to iterate through the array ------------------------------------------------
# def printThroughArray():
#     for search in searchesUni:
#         if (search == "University of Central Lancashire"):
#             break
#         print(search)

# printThroughArray()

current_time = datetime.now()

print("current time: ", current_time)
# ------------------------------------------------ searching script function ------------------------------------------------
def searchInputUni():
    for search in searchesUni:
        print("Searching for: " + search)
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            search_box.send_keys(Keys.PAGE_DOWN)                     # `¯\_(ツ)_/¯`
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

# ------------------------------------------------ searching script function video games ------------------------------------------------
def searchInputGames():
    for search in gamesSearches:
        print("Searching for: " + search)
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)                               #if it goes too fast microsoft servers can't keep up
            search_box.send_keys(Keys.PAGE_DOWN)                    
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred: {e}")

# ------------------------------------------------ rewards page function ------------------------------------------------
def rewardsPage():
  for element in RewardsPageElements:
      print("Finding element: " + element)
      try:
          click_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_loacted((By.LINK_TEXT, element))
          )
          click_element.click()
          time.sleep(5)
      except Exception as e:
            print(f"An error occurred: {e}")

driver = webdriver.Edge()

# ------------------------------------------------ inputting searches into bing ------------------------------------------------
print("Navigating to Bing")
driver.get("https://www.bing.com")  

searchInputUni()
searchInputGames()

# automatting the clicks on the rewards page
print("Navigating to Microsoft Rewards")
driver.get("https://rewards.bing.com/?signin=1&FORM=WSBREW&cvid=b62d7f12ed2b4fcab824e14d9e17ca52&ref=WSB")

rewardsPage()

# ------------------------------------------------------------------------------- ELEMENTS ------------------------------------------------
# <div id="ma-card-link" class="actionLink ng-scope x-hidden-vp1" ng-class="{'x-hidden-vp1' : $ctrl.areaConfig.isMobileViewModeEnabled}" ng-hide="$ctrl.isDenseDashboard()" ng-if="item.exclusiveLockedFeatureCardStatus != 'locked'">
        #     <span class="pointLink ng-binding">
        #         Convert now &gt;
        #     </span>
        # </div>
