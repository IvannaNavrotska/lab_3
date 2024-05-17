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

    def handle(self, shape):
        if self._next_handler:
            return self._next_handler.handle(shape)
        return None


class CubeHandler(AbstractHandler):
    
    def handle(self, shape):
        if shape['type'] == 'cube':
            if shape['height'] < 0:
                return 'Error: height cannot be negative'
            volume = shape['height'] ** 3
            return f'The volume of your cube is: {volume}'
        else:
            return super().handle(shape)


class CylinderHandler(AbstractHandler):
    
    def handle(self, shape):
        if shape['type'] == 'cylinder':
            if shape['radius'] < 0 or shape['height'] < 0:
                return 'Error: radius and height cannot be negative'
            volume = 3.14 * (shape['radius'] ** 2) * shape['height']
            return f'The volume of your cylinder (maybe snake) is: {volume}'
        else:
            return super().handle(shape)


class SphereHandler(AbstractHandler):
    
    def handle(self, shape):
        if shape['type'] == 'sphere':
            if shape['radius'] < 0:
                return 'Error: radius cannot be negative'
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
        
    elif shape_type == 'snake':
        
        print('Sorry, we cannot calculate the volume of a snake\n'
              'But we can imagine your snake as a cylinder.')
        answer = input('Is it an acceptable option? (yes or no): ')
        
        if answer == 'yes':
            radius = float(input('Enter the radius of your cylinder base (cm): '))
            height = float(input('Enter the height of your cylinder (cm): '))
            shape = {'type': 'cylinder', 'radius': radius, 'height': height}
        else:
            print("Thanks for your choice. We hope your snake isn't very upset.")
            return
            
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
