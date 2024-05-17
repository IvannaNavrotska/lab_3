import unittest
from code import *


class TestShapeHandlers(unittest.TestCase):
    
    def setUp(self):
        self.cube = CubeHandler()
        self.cylinder = CylinderHandler()
        self.sphere = SphereHandler()
        
        self.cube.set_next(self.cylinder).set_next(self.sphere)

    def test_cube_handler(self):
        shape = {'type': 'cube', 'height': 3}
        result = self.cube.handle(shape)
        self.assertEqual(result, 'The volume of your cube is: 27')

    def test_cylinder_handler(self):
        shape = {'type': 'cylinder', 'radius': 3, 'height': 4}
        result = self.cube.handle(shape)
        self.assertEqual(result, 'The volume of your cylinder (maybe snake) is: 113.04')

    def test_sphere_handler(self):
        shape = {'type': 'sphere', 'radius': 2}
        result = self.cube.handle(shape)
        self.assertEqual(result, 'The volume of your sphere is: 33.49333333333333')

    def test_unknown_shape(self):
        shape = {'type': 'unknown'}
        result = self.cube.handle(shape)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
