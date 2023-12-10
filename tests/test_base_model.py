#!/usr/bin/python3
"""Test module for BaseModel."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
	"""Define test cases for BaseModel class"""

	def test_init(self):
		my_model = BaseModel()
		self.assertIsInstance(my_model, BaseModel)

	def test_str(self):
		"""Test the __str__ method."""
		my_model = BaseModel()
		str_representation = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
		self.assertEqual(str(my_model), str_representation)

		def test_save(self):
			"""Test the save method."""
		my_model = BaseModel()
		old_updated_at = my_model.updated_at
		my_model.save()
		self.assertNotEqual(old_updated_at, my_model.updated_at)

	def test_to_dict(self):
		"""Test the to_dict method."""
		my_model = BaseModel()
		my_model.name = "My First Model"
		my_model.my_number = 89
		my_model_json = my_model.to_dict()
		self.assertEqual(my_model_json['name'], "My First Model")
		self.assertEqual(my_model_json['my_number'], 89)
		self.assertEqual(my_model_json['__class__'], "BaseModel")


if __name__ == '__main__':
	unittest.main()
