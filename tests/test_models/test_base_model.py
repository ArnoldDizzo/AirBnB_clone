#!/usr/bin/python3
"""Test of BaseModel class"""
import unittest
from models import storage
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel_insatiation(unittest.TestCase):
    """For instatiation of class test"""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_created_obj_stored(self):
        self.assertIn(BaseModel(), storage.all().values())

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_str(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))



if __name__ == "__main__":
    unittest.main()
