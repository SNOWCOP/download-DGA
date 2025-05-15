# download-DGA
Python script using Selenium to scrape and download meteorological data from the DGA (Dirección General de Aguas, Chile) website.

 
This repository contains the necessary files and instructions to set up an environment for using the Selenium. Follow the steps below to get started.

## Cloning the Repository
 
To clone this repository, open your terminal and run the following command:


```bash
git clone git@github.com:SNOWCOP/download-DGA.git
 
cd download-DGA/
 
conda env create -f download_dga.yml
 
conda activate download-DGA
 
spyder
```

Alternatively, you can create your own Conda environment and install the necessary libraries—such as Selenium and Pandas—using Conda. Add any additional dependencies as needed for your setup.



## 🛠 Seeting up the Code
Before running the script, scroll down to the **configuration section** and set the following parameters:

- **`parameter`**  
  The meteorological parameter you want to download (among `"temperature"`, `"snow_height"`, `"SWE"`, `"precipitation"`,`"discharge"` and `"radiation"`).  

- **`download_name`**  
  Full path to the expected download file name (usually where Chrome saves files by default).  
  **Example on Windows:**

  ```python
  download_name = "C:/Users/your_username/Downloads/download.xls"
  ```

- **`outdir`**  
  Directory path where you want the output files to be saved.
Make sure this directory exists or is created before saving.

- **`ids_list`**  
 A Python list containing the station IDs (as strings) you wish to download data for.

- **`date_list`**  
  This variable is automatically loaded from a text file and contains the list of date ranges used for data downloads.

  When working with **daily resolution**, the total date range is divided into smaller chunks of approximately **330 days**, which is the **maximum period allowed per request** by the DGA website.

### ▶️ Running the Script

Once you have modified the configuration parameters, you can run the script.

If everything is working correctly, a **CAPTCHA** will appear after a short delay. On **Windows**, this is signaled by a **notification sound**.

> **Note:** You do **not** need to solve the CAPTCHA. Simply **click on the orange icon** to continue the process.

<p align="center">
  <img src="images/captcha-1.PNG" alt="Date list format example" width="400"/>
</p>

Do this as many times as needed until the CAPTCHA is cleared, also eventually by refreshing the CAPTCHA and the script proceeds.

<p align="center">
  <img src="images/captcha-2.PNG" alt="Date list format example" width="400"/>
</p>

Press ENTER in your Python console and the script will continue!
In the unfortunate case the website crashes or something went wrong, restart the script.



