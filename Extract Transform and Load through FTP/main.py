import sys                                      # For accessing command-line arguments
import json                                     # For loading JSON configuration  
import time                                     # For sleeping the process (used in scheduling loop)
import schedule                                 # For scheduling the pipeline to run at specific times
import pandas as pd                             # For reading and working with CSV files
from os import environ, remove                  # For accessing environment variables and deleting files
from pathlib import Path                        # For handling file paths in a clean, OS-independent way
from ftplib import FTP_TLS                      # For secure FTP connection using TLS

# Function to establish and return a secure FTP connection
def get_ftp() -> FTP_TLS:
    # Get FTP details
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASSWORD"]

    #Return authenticated FTP
    #Create FTP_TLS object and login with credentials (Encrypting the credentials)
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    #Encrypting the file content
    ftp.prot_p()
    # Return the authenticated and secured FTP connection
    return ftp

# Function to upload a file to FTP
def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    # Open the file in binary read mode
    with open(file_source, "rb") as fp:
        # Upload the file to FTP using its filename
        ftp.storbinary(f"STOR {file_source.name}", fp)

# Function to delete a file from the local filesystem
def delete_file(file_source: str | Path):
    remove(file_source)                 # Delete the file using its path

# Function to read a CSV file using a given config dictionary
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]                 # Extract the URL from the config
    params = config["PARAMS"]           # Get additional read parameters (e.g., column names, engine)
    return pd.read_csv(url, **params)   # Return the loaded DataFrame using pandas

# Main pipeline function
def pipeline(): 
    # Open and load the configuration JSON file containing all CSV source info
    with open(".\Extract Transform\config.json", "rb") as fp:
        config = json.load(fp)

     # Establish FTP connection
    ftp = get_ftp()

    #Loop through each configuration to get the source_name and its corresponding config
    for source_name, source_config in config.items():
        # Create a file name using the source name with .csv extension
        file_name = Path(source_name + ".csv")

        # Download and read the CSV into a DataFrame
        df = read_csv(source_config)

        # Save the DataFrame as a local CSV file (without index)
        df.to_csv(file_name, index=False)

        # Print confirmation of file creation
        print(f"File {file_name} has been downloaded created")

        # Upload the CSV file to the FTP server
        upload_to_ftp(ftp, file_name)
        print(f"File {file_name} has been uploaded to FTP")

        # Delete the local file after upload
        delete_file(file_name)
        print(f"File {file_name} has been deleted")


# Entry point of the script
if __name__ == "__main__":
    # Get the first command-line argument passed to the script
    param = sys.argv[1]
    # If 'manual' is passed, run the pipeline once
    if param == "manual":
        pipeline()
    # If 'schedule' is passed, run the pipeline every day at 19:04 or to any requirement time
    elif param == "schedule":
        schedule.every().day.at("19:04").do(pipeline)

        # Keep the program running and check the schedule every second
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    # If an invalid parameter is passed, print usage instructions and exit
    else:
        print("Invalid parameter. Use 'manual' or 'schedule'.")
        sys.exit(1)
