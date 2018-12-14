#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
*TL;DR80
Data management classes.
"""
import pandas as pd
import psycopg2
import pandas.io.sql as sqlio

class Connection(object):
    """ Data base connection Class """

    conn = None

    def __init__(self, host, db, usr, pwd):
        self.conn = psycopg2.connect(host=host, database=db, user=usr, password=pwd)

    def run_query(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            cur.close()
            self.conn.commit()
        except:
          return False
        return True

    def query_data(self, sql):
        rs = None
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
        except:
            return None
        return rs

    def query_data_frame(self, sql):
        df = sqlio.read_sql(sql, self.conn)
        return df

    def close(self):
        self.conn.close()

    def test_query(self):
        return self.query_data('select 10')

class Data(object):
    """ Data Store Class """
    sales_per_product = None

    def __init__(self):
        self.con = Connection('host', 'postgres', 'postgres', 'senha')

    def get_str_from_file(self, file_name):
        with open(file_name, 'r') as myfile:
            str = myfile.read()
        return str

    def fetch_data(self):
        query = self.get_str_from_file('queries/sales_per_day.sql')
        self.sales_per_product = self.con.query_data_frame(query)
