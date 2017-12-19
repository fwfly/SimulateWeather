
BASE_PRESSURE = 1013
REDUCE_PHA_PER_HEIGHT = 100

def get_pressure(ele):

    '''
    get pressure by elevation

    param ele: elevation
    type ele: Int

    return press hPa
    '''

    return BASE_PRESSURE - ( ele/900 )*REDUCE_PHA_PER_HEIGHT

if __name__ == '__main__':
    print "Test Pressure"
    print get_pressure(6900) # Aconcagua
