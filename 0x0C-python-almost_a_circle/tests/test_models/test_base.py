import unittest
from models.base import Base

class TestBaseMethods(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
    
    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    
    def test_nb_objects(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
    
    def test_id_multiple(self):
        b1 = Base()
        b2 = Base(80)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 80)
        self.assertEqual(b3.id, 2)
    
    def test_no_of_input(self):
        with self.assertRaises(TypeError):
            b1 = Base(2,2)
    
    def test_private_attr(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

if __name__ == '__main__':
    unittest.main
