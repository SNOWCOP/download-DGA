# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime as dt
from datetime import timedelta
import pandas as pd

import os
import shutil

if os.name == 'nt':
    import winsound  # Libreria per emettere suoni su Windows
 



"""
Script to automatically download meteorological data from 
the Direción General de Aguas (DGA) - Chile
https://snia.mop.gob.cl/dgasat/pages/dgasat_main/dgasat_main.htm
"""


def select_parameters(station_name, date_start, date_end, parameter, outdir,
                      download_name):
    
    par_dic = {"temperature" : "Temp.del Aire",
               "snow_height" : "Altura de Nieve",
               "SWE" : "Equiv. en agua",
               "precipitation" : "Pptación",
               "discharge" : "Caudal",
               "radiation" : "Rad.Solar"} 


    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Safari/537.36"')

    # chrome_options.add_argument(r'--load-extension=')
    chrome_options.add_extension(r'3.1.0_0.crx')

    driver = webdriver.Chrome(options=chrome_options)


    # connect to the website
    url = r'https://snia.mop.gob.cl/dgasat/pages/dgasat_param/dgasat_param.jsp?param=1'
    driver.get(url)


    # station code and period
    myID = station_name.split(' ')[0]
    d1 = dt.strftime(dt.strptime(date_start, "%d/%m/%Y"),format="%Y%m%d")
    d2 = dt.strftime(dt.strptime(date_end, "%d/%m/%Y"),format="%Y%m%d")
    
    # check if the file has already been downloaded
    filename = outdir + os.sep + ('_').join([myID, d1, d2]) + '.xls'
    
    if os.path.exists(filename):
        print(filename + ' already downloaded!')
        return
    
    # select the station
    select = Select(driver.find_element(By.NAME,'estacion1'))
        
    print('Selecting station ' + station_name)
    select.select_by_value(station_name.split(' ')[0])                                           

    
    # view available parameters
    driver.find_element(By.NAME,'button2').click()
    
    time.sleep(2)
    

    # check reCAPTCHA
    driver.switch_to.default_content()
    driver.find_element(By.XPATH,"//iframe[@title='reCAPTCHA']").click()
  
    time.sleep(2)

    


    try:
        # Check for the main reCAPTCHA checkbox
        checkbox = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"//iframe[@title='recaptcha challenge expires in two minutes']"))
        )
        if checkbox.is_displayed():
            print("reCAPTCHA to be solved manually is detected.")
            
            if os.name == 'nt':
                winsound.Beep(1000, 100)
                winsound.Beep(1000, 100)
                winsound.Beep(1000, 100)
            
            # Wait for the user to solve the reCAPTCHA and press Enter
            input("\n✅  Press Enter after solving the reCAPTCHA...")
            print("✅  Continuing execution...\n")
        
    except:
        pass  
        
    time.sleep(2)       

    
    # Find all available parameters for the selected station - Checkboxes
    checkbox_elements = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    
    time.sleep(2)
    
    # Create a list to store checkbox values
    checkbox_values = []
    
    param_flag = False
    # Iterate through the checkboxes
    for checkbox in checkbox_elements:
        
        # Get the value or label of the checkbox and add it to the list
        value = checkbox.get_attribute("value")  # You can also use .text if the label is not in the "value" attribute
        checkbox_values.append(value)

        if par_dic[parameter] in value:
            checkbox.click()
            
            param_flag = True
            time.sleep(2)


    # select the datat type (temporal resolution)
    driver.find_element(By.XPATH,"//input[@onchange='sinop()']").click()

    time.sleep(2)
    
    # Now change the dates!!
    
    # Find the date input field for the start date
    date_input_start = driver.find_element(By.NAME, "fechaInicioTabla")  # Replace with the actual name/ID
    date_input_end = driver.find_element(By.NAME, "fechaFinTabla")  # Replace with the actual name/ID

    # date start
    date_input_start.clear()  # Clears the content (optional)
    
    date_input_start.send_keys(Keys.ENTER)
    time.sleep(2)

    date_input_start.send_keys(Keys.CONTROL, 'a')  # Select all content (for Windows/Linux)
    time.sleep(2)
    
    date_input_start.send_keys(date_start)
    time.sleep(2)
    
    # date end
    date_input_end.send_keys(Keys.ENTER)
    time.sleep(2)


    date_input_end.send_keys(Keys.CONTROL, 'a')  # Select all content (for Windows/Linux)
    time.sleep(2)

    date_input_end.send_keys(date_end)
    time.sleep(2)
    

    
    # DOWNLOAD
    driver.find_element(By.NAME,'button22').click()
    
    time.sleep(2)
    driver.find_element(By.NAME,'button2').click()
    time.sleep(2)
    
    driver.find_element(By.NAME,'boton4').click()
    
    time.sleep(2)
    shutil.move(download_name, filename)
    return












if __name__ == "__main__":
        
    #--------------------------------------------------------------------
    # select among the available parameters, the one you want to download
    parameter = "discharge"

    # path to the folder where the file is initially downloaded automatically 
    # (default download folder)
    # download_name = r'C:\Users\WPremier\Downloads\download.xls'
    download_name = r'/home/vpremier/Downloads/download.xls'

    
    # out directory 
    # outdir = r'X:\MRI_Andes\Dati\Cile\SWE_AOI_notmerged'
    outdir = r'/mnt/CEPH_PROJECTS/PROSNOW/MRI_Andes/Dati/Cile/Q'

    
    # list with the ids of the stations to be downloaded
    # ids_list = [ '05401007-9', '05703009-7', '04511004-4', '07301000-4','08372001-8','08374001-9']
    #'04700002-5'
    ids_list = ['03430003-8']
    
    date_list = pd.read_csv(os.path.join(os.getcwd(),'date_list.txt'), header=None)[0].to_list()



    
    
    for station_name in ids_list:
        
        
        # period for the download
        for date_start_str in date_list:
     
            #--------------------------------------------------------------------
            
            # Convert to datetime object
            date_start = dt.strptime(date_start_str, "%d/%m/%Y")
            
            # Subtract 330 days (ca. max period allowed for the downloading)
            date_end = date_start + timedelta(days=330)
            
            # Convert back to string if needed
            date_end_str = date_end.strftime("%d/%m/%Y")
            
            print("date_start:", date_start_str)
            print("date_end:", date_end_str)
            
            
    
            select_parameters(station_name, date_start_str, date_end_str, parameter, outdir,
                                  download_name)
          







