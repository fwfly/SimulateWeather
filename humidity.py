'''
humidity :  compute adjust elevation  to check if there is sea.
If adject item is sea humidity +10, if it is lend -3 with a randon base humidity
'''

from random import randint

def get_humidity(lat, log, geo_map):
    '''
    compute humidity by geography

    param lag : latitude from -90 to 90
    type lag : Int
    param log : longitude from -180 to 180
    type log : Int
    param geo_handler: openCV img object
    type geo_handler: 2D List

    return humidity
    '''

    humidity = randint(0, 100)

    height, width = geo_map.shape
    y = 90 - lat
    x = 180 + log
    # change it into map position
    y = int((y/180) * height)
    x = int((x/360) * width)

    for iy in range(y-2, y+2):
        for ix in range(x-2, x+2):
            if geo_map[iy, ix] == 0:
                humidity += 10
            else:
                humidity -= 3
    if humidity > 100:
        return 100

    if humidity < 0:
        return 0

    return humidity

if __name__ == '__main__':

    import geo_helper
    geo = geo_helper.GeoHelper()
    geo.read_map("elevation.bmp")
    print get_humidity(-33.86, 151.21, geo.get_geo_map())
