# opencv-shape-and-color-detection
Shape, Color, Area, and Centroid calculation of all objects present in an image, and arranging them in decreasing order of area in a dictionary which includes all the above said data as values.

Modules used are opencv and numpy

for beginners, install these modules by using following commandline in cmd
pip install opencv-python
pip install numpy

In this project, only three colors namely Red, Green, and Blue are detected. You can add more color detection by importing colors.csv file (which contains RGB values of 865 color shades) using pandas library.
Color is identified by calculating distance to the standard colors, and is assigned the color name to which the distance is the least

First image is converted to gray scale by cv2.
And a threshold is applied to distinguish lighter and darker area.
Then a contour is drawn around the shape, and collection of coordinates is saved to the variable 'contours'
Shape is identified by counting the number of corners in the approximation of contour drawn around the shape.
First item in contour list is deleted (because it is the coordinated of the boundary of the whole image itself)
While iterating through each contour in countours list, countours are approximated to polygons using cv2.approxPolyDP function.
Counting the number corners, different polygons are identified.
For 4 sided polygons; all sides, diagonal, and slope of sides are calculated. square, rectangle, rhombus, parallelogram, trapezium, quadrilateral are further classified, refer the code for more information.

Area is found by function cv2.contourArea()
Centriods are calculated by first calculating moments of the shape using cv2.moments() function.
A list [color name, area, x coordinate of centroid, y coordinate of centroid] is assigned as value for key 'shape' to the dictionary

dictionary is converted to list for the purpose of re-arranging based on decreasing order of area by list(dict.items()) function
a loop is used to execute this sorting
list is converted back to dictionary by dict() function



