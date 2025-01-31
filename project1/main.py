import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# will place into seperate file later on
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
    "University of the London",
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

# same with this one
RewardsPageElements = [
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
#     for search in searches:
#         if (search == "University of Central Lancashire"):
#             break
#         print(search)

# printThroughArray()

current_time = datetime.now()

print("current time: ", current_time)
# ------------------------------------------------ searching script function ------------------------------------------------
def searchInput():
    for search in searchesUni:
        print("Searching for: " + search)
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(search)
            search_box.send_keys(Keys.RETURN)
            time.sleep(2)
            search_box.send_keys(Keys.PAGE_DOWN)                     # `¯\_(ツ)_/¯`
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
          time.sleep(2)
      except Exception as e:
            print(f"An error occurred: {e}")

driver = webdriver.Edge()

# ------------------------------------------------ inputting searches into bing ------------------------------------------------
print("Navigating to Bing")
driver.get("https://www.bing.com")  

searchInput()

# automatting the clicks on the rewards page
print("Navigating to Microsoft Rewards")
driver.get("https://rewards.bing.com/?signin=1&FORM=WSBREW&cvid=b62d7f12ed2b4fcab824e14d9e17ca52&ref=WSB")

rewardsPage()

# ------------------------------------------------ Microsoft Rewards script --------------------------------------------------------------------------
#def():

# print("Navigating the Microsoft Rewards...")
# driver.get("https://rewards.bing.com/?signin=1&FORM=WSBREW&cvid=b62d7f12ed2b4fcab824e14d9e17ca52&ref=WSB")

# ------------------------------------------------------------------------------- ELEMENTS ------------------------------------------------
# <div id="ma-card-link" class="actionLink ng-scope x-hidden-vp1" ng-class="{'x-hidden-vp1' : $ctrl.areaConfig.isMobileViewModeEnabled}" ng-hide="$ctrl.isDenseDashboard()" ng-if="item.exclusiveLockedFeatureCardStatus != 'locked'">
        #     <span class="pointLink ng-binding">
        #         Convert now &gt;
        #     </span>
        # </div>