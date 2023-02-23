import configparser
import os
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + "/utilities/properties.ini")
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}


def getPass():
    return 'Inf@1238$2012'


def getConnection():
    try:
      conn = mysql.connector.connect(**connect_config)
      if conn.is_connected():
          print("connetion is succesfull ")
          return conn
    except Error as e:
        print(e)



