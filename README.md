

# On-Premise Data Pipeline and Machine Learning deployment



## Project Overview

![Project Overview](/images/diagram.png)

## Data Pipeline from the web to FTP server

- Set up WSL to have a Linux Environment with different OS by using command-line interpreter
- Installed vsftpd (to create our own local FTP server) and adjusted its configuration.
- Set up a Python development environment.
- Estabish a connection to an FTP server 
- Created a pipeline for data extraction from the web and clean the data format(-0- to null, added header) then upload those data to FTP server.
- Wrote a script for manual or scheduled execution of the task.

    [Documentation for Data Pipeline from the web to FTP server](https://github.com/Miraiumxdd/on-premise-data-pipeline-ml-deployment/tree/main/Extract%20Transform%20and%20Load%20through%20FTP)

## From FTP server to Postgre

- This project demonstrates a complete ETL process using SSIS (SQL Server Integration Services).

- It involves transferring data from an FTP server to PostgreSQL (or SQL Server).

- Includes VSFTPD reconfiguration to allow FTP connections for SSIS.

- Before loading data into database all tables are truncated to full load the data. 

- Data is loaded into a PostgreSQL database and transformed data into merged final table for further use.

    [Documentation for pipeline From FTP server to Postgre](https://github.com/Miraiumxdd/on-premise-data-pipeline-ml-deployment/tree/main/ftptopostgre)










