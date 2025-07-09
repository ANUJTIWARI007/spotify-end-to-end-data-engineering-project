# Spotify-End-To-End-Data-Engineering-Project

### Introduction

In this project, we will build an ETL (Extract , Transform , Load) pipeline using the spotify API on AWS. The pipeline will retrieve data from the spotify API, Tansform it to a desire format, and load it into an AWS data store.

### Architecture
![Architecture Diagram](https://github.com/ANUJTIWARI007/spotify-end-to-end-data-engineering-project/blob/main/Architecture_Diagram.jpg)

### About Dataset/API
This API contains information about music artist , albums and songs - [Spotify API Doc](https://spotipy.readthedocs.io/en/2.25.1/)

### Services Used 
1. **S3 (Simple Storage Service):** Amazon S3 (Simple Storage Service) is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web . It is commonly used to store and distribute large media file, data backups, and static website files.

2. **AWS Lambda:** AWS Lambda is a serverless computing service that lets you run your code without managing servers. you can use Lambda to run code in response to events like changes in S3 , DynamoDB, or other AWS services.

3. **Cloud Watch:** Amazon CloudWatch is monitoring service for AWS resources and the applications you can run on them. you can use cloudwatch to collect and track the metrics , collect and monitor log files ,and set alarms.

4. **Glue crawler:** AWS Glue crawler is fully managed service that automatically crawls your data sources , identifies data format , and infers schemas to create an AWS Glue Data Catalog.

5. **Data Catalog:** AWS Glue Data Catalog is fully managed metadata repository that makes easy to discover And manage data in AWS you can use the Glue Data catalog with other AWS services, such as Athena.

6. **Amazon Athena:** Amazon Athena is an interactive query service that makes it easy to analyze data in amazon S3 using standard SQL. you can use Athena to analyze data in your Glue data catalog or in other S3 bucket .

### Install packages 
```
pip install pandas as pd 
pip install numpy 
pip install spotipy 
```
### Project Execution Flow 
Extract Data from API -> Lambda Trigger (every 1 day ) -> run extract Code -> Store Raw Data -> Trigger Transform Function -> Transform data and Load it -> Query using athena 

