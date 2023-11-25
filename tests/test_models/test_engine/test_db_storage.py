#!/usr/bin/python3
import unittest
import MySQLdb
from models.user import User
from models import test_db_storage
from datetime import datetime
import os 


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
        'fileStorage test not supported')
class TestDBStorage(unittest.TestCase):
    ''' Testing database'''
    def test_new_and_save(self):
        '''Testing the new and save methods'''
        db = MySQLdb.connect(user=os.getenv('HBNB_TYPE_USER'),
                host=os.getenv('HBNB_MYSQL_HOST'),
                passwd=os.getenv('HBNB_MYSQLPWD'),
                port=3306,
                db=os.getenv('HBNB_MYSQL_DB'))
        new_user = User(**{'first_name': 'Jack',
            'last_name': 'bond',
            'email': 'jack@bond.com',
            'password': 12345})
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchone()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=os.getenv('HBNB_TYPE_USER'),
                host=os.getenv('HBNB_MYSQL_HOST'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                post=3306,
                db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchone()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()

    def test_new(self):
        """ New object is correctly added to the database"""
        new = User(
                email='john2020@gmail.com',
                password='password',
                first_name='John',
                last_name='Zoldyck'
                )
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                post=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
                )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE ID="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)
        cursor.close()
        dbc.close()

    def test_delete(self):
        ''' test'''
        new = User(
                email='john2020@gmail.com',
                password='password',
                first_name='John',
                last_name='Zoldyck'
                )
        obj_key = 'User.{}'.format(new.id)
        dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                post=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
                )
        new.save()
        self.assertTrue(new in storage.all().values())
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('john2020@gmail.com', result)
        self.assertIn('password', result)
        self.assertIn('John', result)
        self.assertIn('Zoldyck', result)
        self.assertIn(obj_key, storage.all(user).keys())
        new.delete()
        self.assertNotIn(obj_key, storage.all(user).keys())
        cursor.close()
        dbc.close()

 def test_reload(self):
     """Tests for reloading"""
     dbc = MYSQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
            )
    cursor = dbc.cursor()
    cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '4447-by-me',
                str(datetime.now()),
                str(datetime.now()),
                'ben_pike@yahoo.com',
                'pass',
                'Benjamin',
                'Pike',
                ]
            )
    self.assertNotIn('User.4447-by-me', storage.all())
    dbc.commit()
    storage.reload()
    self.assertIn('User.4447-by-me', storage.all())
    cursor.close()
    dbc.close()

def test_save(self):
    """Tests for saving"""
    new = User(
            email='john2020@gmail.com',
            password='password',
            first_name='John'
            last_name='Zoldyck'
            )
    dbc = MYSQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
            )
    cursor = dbc.cursor()
    cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
    result = cursor.fetchone()
    old_cnt = cursor.fetchone()[0]
    self.assertTrue(result is None)
    self.assertFalse(new in storage.all().values())
    new.save()
    dbc1 = MYSQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
            )
    cursor1 = dbc1.cursor()
    cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
    result = cursor1.fetchone()
    cursor1.execute('SELECT COUNT(*) FROM users;')
    new_cnt = cursor1.fetchone()[0]
    self.assertFalse(result is None)
    self.assertEqual(new in storage.all().values())
    cursor1.close()
    dbc1.close()
    cursor.close()
    dbc.close()
