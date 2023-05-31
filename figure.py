'''
figure 모듈은 도형에 관련된 함수 및 클래스를 제공하는 모듈입니다.
line 클래스를 통해 선의 길이에 대해 수정 및 접근하여 
직사각형, 타원, 직각삼각형의 넓이를 구할 수 있습니다.
'''

import math

class line:
    '''
    line 클래스는 다양한 선의 길이를 저장하는 클래스입니다.
    외부에서 접근 불가능한 __witdh와 __height가 있습니다.
    해당 변수들에 접근하고 수정하기 위해 set_length 메소드와 get_length 메소드를 제공합니다.
    '''
    __width = 0
    __height = 0
    def __init__(self, width, height):
        ''' 생성자를 통해 초기 width와 height값을 설정합니다.
        Args:
            width (int or float): 초기 가로 길이
            height (int or float): 초기 세로 길이
        '''
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        ''' 선의 길이를 수정합니다.
        Args:
            width (int or float): 수정하고자 하는 가로 길이
            height (int or float): 수정하고자 하는 세로 길이
        '''
        self.__width = width
        self.__height = height

    def get_length(self):
        ''' 객체가 가지고 있는 선의 길이 값을 반환합니다.
        Returns:
            (int or float): 저장하고 있는 선의 길이
        '''
        return self.__width, self.__height

def area_rectangle(width, height):
    ''' 선의 길이를 입력받아 직사각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 직사각형 가로의 길이
        height (int or float): 직사각형 세로의 길이
    Returns:
        (int or float): 직사각형의 넓이
    '''
    if width <= 0  or height <=0: raise ValueError
    return width * height

def area_ellipse(width, height):
    ''' 선의 길이를 입력받아 타원의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 타원 장축의 길이
        height (int or float): 타원 단축의 길이 
    Returns:
        (int or float): 타원의 넓이
    '''
    if width <= 0  or height <=0: raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    ''' 선의 길이를 입력받아 직각삼각형의 넓이를 구하는 함수입니다.
    Args:
        width (int or float): 직각삼각형 밑변의 길이 
        height (int or float): 직각삼각형 높이의 길이
    Returns:
        (int or float): 직각삼각형의 넓이
    '''
    if width <= 0  or height <=0: raise ValueError
    return (width * height) / 2