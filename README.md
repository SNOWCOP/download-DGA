# download-DGA
Python script using Selenium to scrape and download meteorological data from the DGA (Dirección General de Aguas, Chile) website.

 
This repository contains the necessary files and instructions to set up an environment for using the Selenium. Follow the steps below to get started.

## Cloning the Repository
 
To clone this repository, open your terminal and run the following command:

For Ubuntu os:
```bash
git clone git@github.com:SNOWCOP/download-DGA.git
 
cd download-DGA/
 
conda env create -f download_dga.yml
 
conda activate download-DGA
 
spyder
```

For Windows os:



## 🛠 Running the Code
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

<p align="center">
  <img src="images/captcha-1.PNG" alt="Date list format example" width="400"/>
</p>


