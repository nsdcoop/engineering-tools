'''
Tools to add:
    Virial equation
    Lee/Kesler table lookup
    Property table lookup?
    Enthalpy/heat capacity calculator
'''

def my_interp2d(point, x, y, z):
    '''x represented by rows in z, y represented by columns in z'''
    x1, x2 = x
    y1, y2 = y
    ((x1y1, x1y2), (x2y1, x2y2)) = z
    xx, yy = point

    # interpolate in x
    yy1 = (xx - x1)/(x2 - x1) * (x2y1 - x1y1) + x1y1
    yy2 = (xx - x1)/(x2 - x1) * (x2y2 - x1y2) + x1y2

    # interpolate in y
    return (yy - y1)/(y2 - y1) * (yy2 - yy1) + yy1

def virial_pitzer(Tr, Pr, w):
    '''Virial equation with Pitzer correlation for second coefficient'''
    B0 = 0.083 - 0.422/Tr**1.6
    B1 = 0.139 - 0.172/Tr**4.2
    return 1 + B0*Pr/Tr + w*B1*Pr/Tr
