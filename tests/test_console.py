#!/usr/bin/python3
""" UnitTest Module """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestConsole(unittest.TestCase):
    """ Test Console class """

    test_model = BaseModel()

    def testClassInstance(self):
        """ Check if is instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save, reload and update functions """
        """ Test attributes value of a BaseModel instance """

        self.test_model.name = "My_First_Model"
        self.test_model.my_number = 89
        self.test_model.save()
        test_model_json = self.test_model.to_dict()

        self.assertEqual(self.test_model.name, test_model_json['name'])
        self.assertEqual(self.test_model.my_number, test_model_json['my_number'])
        self.assertEqual('BaseModel', test_model_json['__class__'])
        self.assertEqual(self.test_model.id, test_model_json['id'])

    def testHasAttributes(self):
        """ verify attributes existance """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testSave(self):
        """verify if JSON exists"""
        self.test_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)
 
    def testSaveSelf(self):
        """ Check save self """
        phrase = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), phrase)

if __name__ == '__main__':
    unittest.main()
