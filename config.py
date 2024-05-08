# Databricks notebook source
snowflake_conn_prop = {
   "account": "your snowflake account locator",
   "URL": "<Check the example at the bottom>.snowflakecomputing.com",
   "user": "username",
   "password": "your-password",
   "role": "Snowflake Role name",
   "database": "DBNAME",
   "schema": "SCHEMA",
   "warehouse": "warehouse name",
}

# Snowflake Account Identifiers
# https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#account-identifier-formats-by-cloud-platform-and-region
#  

 #If the account is located in the AWS US West (Oregon) region, no additional segments are required 
 # and the URL would be xy12345.snowflakecomputing.com.

#If the account is located in the AWS US East (Ohio) region, additional segments are 
# required and the URL would be xy12345.us-east-2.aws.snowflakecomputing.com


# More on how to setup connection at https://docs.snowflake.com/en/developer-guide/snowpark/python/creating-session.html

