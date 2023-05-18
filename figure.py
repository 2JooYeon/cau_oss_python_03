'''
figure 모듈은 도형에 관련된 함수 및 클래스를 제공하는 모듈입니다.
line 클래스를 통해 선의 길이에 대해 수정 및 접근하여 
정사각형, 원, 정삼각형의 넓이를 구할 수 있습니다.
'''

import math

class line:
    '''
    line 클래스는 선의 길이를 저장하는 클래스입니다.
    외부에서 접근 불가능한 변수 __length가 있습니다.
    해당 변수를 수정하기 위해 set_length 메소드를 제공하고,
    해당 변수에 접근하기 위해 get_length 메소드를 제공합니다.
    '''
    __length = 0

    def __init__(self, length):
        ''' 생성자를 통해 초기 선의 길이 값을 설정합니다.
        Args:
            length (int or float): 초기 선의 길이
        '''
        self.__length = length

    def set_length(self, length):
        ''' 선의 길이를 수정합니다.
        Args:
            length (int or float): 수정하고자 하는 선의 길이
        '''
        self.__length = length

    def get_length(self):
        ''' 객체가 가지고 있는 선의 길이 값을 반환합니다.
        Returns:
            (int or float): 저장하고 있는 선의 길이
        '''
        return self.__length

def area_square(length):
    ''' 선의 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
        length (int or float): 정사각형 한 변의 길이
    Returns:
        (int or float): 정사각형의 넓이
    '''
    return length ** 2

def area_circle(length):
    ''' 선의 길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args:
        length (int or float): 원 반지름의 길이
    Returns:
        (int or float): 원의 넓이
    '''
    return length ** 2 * math.pi

def area_regular_triangle(length):
    ''' 선의 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
        length (int or float): 정삼각형 한 변의 길이
    Returns:
        (int or float): 정삼각형의 넓이
    '''
    return (math.sqrt(3) / 4) * length ** 2