from geometry import *

'''

main
{
    var point1 = new Point(1,2,1);
    var point2 = new Point(0,4,4);
    var vector1 = new Vector(2,0,0);
    var vector2;

    point1.drawPoint(); //должна вывести (1,2,1)
    point2.drawPoint(); //должна вывести (0,4,4)

    vector2 = point1.subtractPointFromPoint(point2);

    vector1 = vector1.addVectorToVector(vector2);

    point1.addVectorToPoint(vector1);
    point1.drawPoint(); //должна вывести (4,0,-2)

    point2.subtractVectorFromPoint(vector2);
    point2.drawPoint(); //должна вывести (-1,6,7)
}

'''

point1 = point(1, 2, 1)
point2 = point(0, 4, 4)

vector1 = vector(2, 0, 0)

print(point1.draw())
print(point2.draw())