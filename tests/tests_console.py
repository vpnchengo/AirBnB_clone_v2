#!/usr/bin/python3
"""The console test"""
import os
import json
import console
import test
import pep8
import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage 
from models.review import Review 
from models.place import Place 
from models.amenity import Amenity 
from models.city import City 
from models.state import State 
from models.user import User 
from models.base_model import BaseModel 
from console import HBNBCommand 

class TestConsole(unittest.TestCase):
    """tests the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')



