#!/usr/bin/python3
"""test for amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


class test_Amenity(test_basemodel):
    """Test Class amenity """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """To test the amentities attribute """
        new = self.value(name="Amenities")
        self.assertEqual(type(new.name), str)

    def testDocumentation(self):
        """compares the documentaion"""
        self.assertTrue(len(Amenity.__doc__) > 0)
        for method in dir(Amenity):
            self.assertTrue(len(method.__doc__) > 0)

    def test_pycodestyle(self):
        """Test for pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors amd warnings).")
