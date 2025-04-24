# Setup Summary: FTP to PostgreSQL/SQL Server via SSIS

This document provides a step-by-step guide on setting up an ETL pipeline that extracts data from an FTP server, transforms it, and loads it into a PostgreSQL or SQL Server database using SQL Server Integration Services (SSIS). It includes configuring the FTP server, building the SSIS package, and deploying it for automation.

---

## 1. Reconfigure vsftpd (FTP Server Setup)

   1. Open **WSL (Windows Subsystem for Linux)**.
   2. Edit the `vsftpd` configuration file:
      ```bash
      sudo nano /etc/vsftpd.conf
      ```
   Add the following lines to disable SSL (for SSIS to connect smoothly):


```bash
force_local_logins_ssl=NO
force_local_data_ssl=NO
```

## 2. Build the SSIS ETL Pipeline

- Create a new SSIS package

- Connects to the FTP server

- Downloads CSV files

- Stores them in a local directory

- Truncates target tables to it will be full load

- Loads the CSV data into Postgres

- Merges all data into a final table for transformation