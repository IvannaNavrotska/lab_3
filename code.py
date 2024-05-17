from __future__ import annotations
from abc import ABC, abstractmethod

class Handler(ABC):
    
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, shape):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, shape):
        if self._next_handler:
            return self._next_handler.handle(shape)
        return None


class CubeHandler(Handler):
    
    def handle(self, shape):

        if shape['type'] == 'cube':
            volume = shape['height'] ** 3
            return f'The volume of your cube is: {volume}'
        else:
            return super().handle(shape)


class CylinderHandler(Handler):
    
    def handle(self, shape):

        if shape['type'] == 'cylinder':
            volume = 3.14 * (shape['radius'] ** 2) * shape['height']
            return f'The volume of your cylinder is: {volume}'
        else:
            return super().handle(shape)


class SphereHandler(Handler):

    def handle(self, shape):

        if shape['type'] == 'sphere':
            volume = (4 / 3) * 3.14 * (shape['radius'] ** 3)
            return f'The volume of your sphere is: {volume}'
        else:
            return super().handle(shape)

def client_code(handler: Handler) -> None:

    shape_type = input('Select a shape type (cube, cylinder, or sphere): ')
    shape = {}
    
    if shape_type == 'cube':
        height = float(input('Enter the height of your cube: '))
        shape = {'type': 'cube', 'height': height}
        
    elif shape_type == 'cylinder':
        radius = float(input('Enter the radius of your cylinder base: '))
        height = float(input('Enter the height of your cylinder: '))
        shape = {'type': 'cylinder', 'radius': radius, 'height': height}
        
    elif shape_type == 'sphere':
        radius = float(input('Enter the radius of your sphere: '))
        shape = {'type': 'sphere', 'radius': radius}
    
    result = handler.handle(shape)
    if result:
        print(result)
    else:
        print('The shape cannot be handled')


if __name__ == '__main__':
    
    cube = CubeHandler()
    cylinder = CylinderHandler()
    sphere = SphereHandler()

    cube.set_next(cylinder).set_next(sphere)

    client_code(cube)
