from __future__ import annotations
from abc import ABC, abstractmethod

class Handler(ABC):
    
    def __init__(self, next_handler = None):
        self.next_handler = next_handler

    def set_next(self, handler: Handler) -> Handler:
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, shape):
        pass


class CubeHandler(Handler):
    
    def handle_request(self, shape):
        if shape['type'] == 'cube':
            volume = shape['height'] ** 3
            print(f'The volume of your cube is: {volume}')
        elif self.next_handler:
            self.next_handler.handle_request(shape)

class CylinderHandler(Handler):
    
    def handle_request(self, shape):
        if shape['type'] == 'cylinder':
            volume = 3.14 * (shape['radius'] ** 2) * shape['height']
            print(f'The volume of your cylinder is: {volume}')
        elif self.next_handler:
            self.next_handler.handle_request(shape)

class SphereHandler(Handler):

    def handle_request(self, shape):
        if shape['type'] == 'sphere':
            volume = (4 / 3) * 3.14 * (shape['radius'] ** 3)
            print(f'The volume of your sphere is: {volume}')
        elif self.next_handler:
            self.next_handler.handle_request(shape)

if __name__ == '__main__':
    
    cube = CubeHandler()
    cylinder = CylinderHandler()
    sphere = SphereHandler()

    cube.set_next(cylinder).set_next(sphere)

    shape_type = input('Select a shape type (cube, cylinder or sphere): ')
    shape = {}
    if shape_type == 'cube':
        height = float(input("Enter the height of your cube: "))
        shape = {'type': 'cube', 'height': height}
    elif shape_type == 'cylinder':
        radius = float(input("Enter the radius of your cylinder base: "))
        height = float(input("Enter the height of your cylinder: "))
        shape = {'type': 'cylinder', 'radius': radius, 'height': height}
    elif shape_type == 'sphere':
        radius = float(input("Enter the radius of your sphere: "))
        shape = {'type': 'sphere', 'radius': radius}

    cube.handle_request(shape)
