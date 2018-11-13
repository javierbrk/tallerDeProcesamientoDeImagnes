#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
import time
import datetime
import mysql.connector


arg="SACD"



cnx = mysql.connector.connect(host='127.0.0.1',     # your host, usually localhost
                      #port=3306,            # port
                     user="SACD",         # your username
                     password="12345",      # your password
                     database=arg)                # name of the data base
cursor = cnx.cursor()


def _sql_time():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return timestamp



def _SQLexec(query):
    try:
        cursor.execute(_sql_inj(query))
    except Exception as e:
        cnx.rollback()
        return "error1:{}".format(e)

    if (query.find('INSERT') != -1) or query.find('UPDATE') != -1:
        cnx.commit()
    return cursor

def _SQLclose(cursor):
  cursor.close()
  cnx.close()


def _SQL_ext_cnslt(db_name,query):
    if not db_name:
        db_name = "NONE"
    xcnx = mysql.connector(host='127.0.0.1',    # your host, usually localhost
                          #port=3306,            # port
                         user="",         # your username
                         passaword="",      # your password
                         db=db_name)            # name of the data base
    xcursor = xcnx.cursor()
    try:
        xcursor.execute(_sql_inj(query))
    except Exception as e:
        xcnx.rollback()
        xcursor.close()
        xcnx.close()
        return "error1:{}".format(e)
    if (query.find('INSERT') != -1) or query.find('UPDATE') != -1:
        cnx.commit()
    resp = xcursor.fetchall()
    #xcursor.close()
    #xcnx.close()
    return resp

class inicializa_bd(object):
    def __init__(self,vtn):
        self.TN = vtn

    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
        exit(1)


def _sql_inj(iq):
    alert = False
    r=['CREATE', 'DROP', 'ALTER', 'DELETE', 'schema', 'mysql', 'SUBSTRING', 'ASCII', '*/','LENGTH', ';']
    for w in r:
        if iq.find(w) != -1:
            alert = True
    if alert:
#        logg("posible intento SQLINJ en {}".format(iq))
        iq = "NONE S1"

    return iq



#Ecualizacion de solicitudes
qy_rd_lst = "SELECT {} FROM {} ORDER BY {} DESC LIMIT 1";
qy_rd_lst_ms = "SELECT TOP 1 {} FROM {} {} ORDER BY {} DESC"
qy_rd_fst_ms = "SELECT TOP 1 {} FROM {} {} ORDER BY {} ASC"
qy_list_r = "SELECT {} FROM {} WHERE {}"
qy_rd_wtw = "SELECT {} FROM {}"
qy_rd_pro = "SELECT {} FROM {} {}"
qy_update = "UPDATE {} SET {} = {} where {}"
qy_insert = "INSERT INTO {}({}) VALUES({})"
qr_truncate = "TRUNCATE TABLE {}.dbo.{}"
qy_inner_j= "SELECT {} FROM {} INNER JOIN {} ON {} = {} WHERE {}"
qy_d_inner_j = "SELECT {} FROM {} INNER JOIN {} ON {} ={} INNER JOIN {} ON {}= {} WHERE {}"

#Clases
class formato_tabla(object):
  def __init__(self, tabla):
      self.table = tabla
      self.field = []
      self.key = ''
      self.proc = ''

  def add_fiel(self, field):
      self.field.append(field)

  def add_key(self, key):
      self.key =key

  def add_proc(self, proc):
      self.proc =proc

  def _txtfld(self):
      return ''.join(self.field)

  def _frmt(self, strqy):
      if self.key == '':
         return strqy.format(''.join(self.field),self.table)
      return strqy.format(''.join(self.field),self.table,self.key)
  def read_all(self):
      if self.key == '':
          return qy_rd_wtw.format(''.join(self.field),self.table)
      else:
          return qy_list_r.format(''.join(self.field),self.table,self.key)

  def read_last(self):
      return qy_rd_lst.format(''.join(self.field),self.table,self.key)

  def read_last_ms(self , aux):
      return qy_rd_lst_ms.format(''.join(self.field),self.table, aux, self.key)

  def read_first_ms(self, aux):
      return qy_rd_fst_ms.format(''.join(self.field),self.table, aux, self.key)

  def read_DISTINCT(self, aux):
      return qy_rd_wtw.format(("DISTINCT {}").format(self.key), ("{} {}".format(self.table, aux)))

  def update_reg(self, val):
      return qy_update.format(self.table,self.field,val,self.key)

  def group_by(self, val):
      return qy_list_r.format(("{}, {}".format(val, ''.join(self.field))), self.table, ("{} GROUP BY ({})".format(self.key, val)))

  def read_proc(self):
      return qy_rd_pro.format(''.join(self.field),self.table,self.proc)

  def insert(self):
      fields =''.join(self.field)
      var2 = ""
      var = "'%s', "
      for a in fields.split(", "):
         var2 = var2 + var
      var2 = var2[:len(var2)-2]

      return qy_insert.format(self.table,fields, var2)

  def inner_join(self, table2, field2,Key1, key2):
      fi =''.join(self.field)
      fi2=''.join(field2)
      t = "{}.{}, "
      v1 = ""
      v2 = ""
      for a in fi.split(", "):
          v1= v1 + t.format(self.table, a)

      for a in fi2.split(", "):
          v2= v2 + t.format(table2, a)

      return qy_inner_j.format("{} {}".format(v1, v2[:len(v2)-2]), self.table, table2, "{}.{}".format(table2, key2), "{}.{}".format(self.table, Key1),self.key )

  def d_inner_join(self, table2, table3,field2, field3, Key1, key1b, key2, key3):
      fi =''.join(self.field)
      fi2=''.join(field2)
      fi3=''.join(field3)
      t = "{}.{}, "
      v1 = ""
      v2 = ""
      v3 = ""
      for a in fi.split(", "):
          v1= v1 + t.format(self.table, a)

      for a in fi2.split(", "):
          v2= v2 + t.format(table2, a)

      for a in fi3.split(", "):
          v3= v3 + t.format(table3, a)

      return qy_d_inner_j.format("{} {} {}".format(v1, v2, v3[:len(v3)-2]), self.table, table2, "{}.{}".format(table2, key2), "{}.{}".format(self.table, Key1), table3, "{}.{}".format(table3, key3), "{}.{}".format(self.table, key1b),self.key  )

  def truncate(self, bd ):
      return qr_truncate.format(bd,self.table)

  def clean(self):
      self.field = []
      self.key = ''








#End
