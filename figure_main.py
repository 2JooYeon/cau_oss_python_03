import figure

myline = figure.line(10, 20)
width, height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("width and height should be positive number")

myline.set_length(20, 30)
width, height = myline.get_length()
try:
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    print("width and height should be positive number")

myline.set_length(30, 40)
width, height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width, height)
    print(ellipse)
except ValueError:
    print("width and height should be positive number")