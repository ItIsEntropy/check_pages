import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import datetime


# Variables:
#           - Offline Sites list that will store offline sites.
#           - Sites that are available in gov

offline_sites = []
sites = ["http://www.sh.gov.zm/", "http://www.ovp.gov.zm/", "http://www.cabinet.gov.zm/", "http://www.psmd.gov.zm/", "http://www.ago.gov.zm/", "http://www.mod.gov.zm/", "http://www.moha.gov.zm/", "http://www.mofa.gov.zm/", "http://www.mof.gov.zm/", "http://www.moj.gov.zm/", "http://www.mndp.gov.zm/", "http://www.agriculture.gov.zm/", "http://www.mfl.gov.zm/", "http://www.mcti.gov.zm/", "http://www.mmmd.gov.zm/", "http://www.moe.gov.zm/", "http://www.mota.gov.zm/", "http://www.mtc.gov.zm/", "http://www.mws.gov.zm/", "http://www.mhid.gov.zm/", "http://www.mlnr.gov.zm/",
         "http://www.mwdsep.gov.zm/", "http://www.moh.gov.zm/", "http://www.mibs.gov.zm/", "http://www.moge.gov.zm/", "http://www.mohe.gov.zm/", "http://www.mlgh.gov.zm/", "http://www.mlss.gov.zm/", "http://www.mcdsw.gov.zm/", "http://www.gender.gov.zm/", "http://www.myscd.gov.zm/", "http://www.mocta.gov.zm/", "http://www.mngra.gov.zm/", "http://www.cen.gov.zm/", "http://www.cbt.gov.zm/", "http://www.eas.gov.zm/", "http://www.lua.gov.zm/", "http://www.lsk.gov.zm/", "http://www.muc.gov.zm/", "http://www.nws.gov.zm/", "http://www.nor.gov.zm/", "http://www.sou.gov.zm/", "http://www.wes.gov.zm/"]

# This is the actual firefox browser as an object
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options = options)

# Make a new folder with todays date - year (%Y), month(%m), and day(%d)
today = (datetime.datetime.now().strftime("%Y%m%d"))
try:
    os.mkdir(today)
except OSError:
    pass

def save_screenshot(driver = webdriver.Firefox, path = './screenshots', include_scrollbar = True):
    '''
        Saves a screenshot of a webpage given the parameters. Parameters include whether r not to include the 
        scrollbar, path to save the image, and the web driver to use.
    '''
    padding = 100

    original_size = driver.get_window_size()
    required_width = driver.execute_script('return document.scrollingElement.scrollWidth')
    required_height = driver.execute_script('return document.scrollingElement.scrollHeight')
    required_width = required_width + padding
    required_height = required_height + padding

    driver.set_window_size(required_width, required_height)
    if include_scrollbar:
        driver.save_screenshot(path)
    else:
        driver.find_element_by_tag_name('body').screenshot(path)
    driver.set_window_size(original_size['width'], original_size['height'])

# Go through the list of sites
# Take snapshots of the site pages
# Save the snapshots inside todays folder

for site in sites:
    try:
        print(f"Getting site: {site}")
        driver.get(site)
        #time.sleep(5)
        path = f"{today}\\{site.split('.')[-3]}.png"
        # driver.save_screenshot(path)
        save_screenshot(driver = driver, path = path, include_scrollbar= False)
    except Exception as e:
        print(f"Failed to get site: \n\t{e}")
        offline_sites.append(site)
driver.close()

# Save the offline sites in a json file
with open('offline_sites.json', 'w+') as f:
    f.write(json.dumps(offline_sites))

'''
if __name__ == '__main__':
    pass
'''