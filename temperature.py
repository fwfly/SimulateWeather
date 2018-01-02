'''
  temperature.py is a module to compute temperature from time, elevation, latitude, longitude.

  formula :
    temperature = initial temperature of season - latitude effect - elevation effect

'''
# Assume -0.2 degree per every latitude
TEMP_PER_LAT = 0.2

ARCTIC_CIRCLE = 66.5
ANTARCTIC_CICLE = -66.5
TROPIC_OF_CANCER = 23.5
TROPIC_OF_CAPRICORN = -23.5


# Initial temperature in 4 season.
# Every zones have their own initial temperature.
SEASON_TEMP_OF_ARCTIC_CIRCLE = [10, 20, 10, 0]
SEASON_TEMP_OF_TROPIC_OF_CANCER = [20, 30, 20, 15]
SEASON_TEMP_OF_EQUATORIAL = [30, 30, 30, 30]
SEASON_TEMP_OF_TROPIC_OF_CAPRICORN = [20, 15, 20, 30]
SEASON_TEMP_OF_ANTARCTIC_CICLE = [10, 0, 10, 20]

# Index in zone initial temperature of every month
SEASON_OF_MONTH = [None, 3, 3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3]

def get_season_init_temp(lat, month):
    '''
    get basic temperature from our season model and calculate with latitude

    param lat : latitude from -90 to 90
    type lat : Int
    param mouth : mouth
    type mouth: Int
    '''

    season = SEASON_TEMP_OF_EQUATORIAL
    tag_position = 0.0
    if lat > 0:
        if lat >= ARCTIC_CIRCLE:
            season = SEASON_TEMP_OF_ARCTIC_CIRCLE
            tag_position = ARCTIC_CIRCLE
        elif lat >= TROPIC_OF_CANCER:
            season = SEASON_TEMP_OF_TROPIC_OF_CANCER
            tag_position = TROPIC_OF_CANCER
    else:
        if lat <= ANTARCTIC_CICLE:
            season = SEASON_TEMP_OF_ANTARCTIC_CICLE
            tag_position = ANTARCTIC_CICLE
        elif lat <= TROPIC_OF_CAPRICORN:
            season = SEASON_TEMP_OF_TROPIC_OF_CAPRICORN
            tag_position = TROPIC_OF_CAPRICORN

    temp_season = season[SEASON_OF_MONTH[month]]

    dis_of_lat = abs(lat) - abs(tag_position)

    # temperature = inital temperature - distance of zone * 0.2
    temp_season = temp_season - dis_of_lat * TEMP_PER_LAT # calculate with latitude

    return temp_season


def get_temp(lat, mouth, ele):
    '''
    based on log, lat, time and ele and return a temperature

    param lat : latitude from -90 to 90
    type lat : Int
    param mouth : mouth
    type mouth: Int
    param ele: elevation
    type ele: Int
    '''

    # pick a season model
    base_temp = get_season_init_temp(lat, mouth)

    # -0.6 TEMP per 100m
    temp = base_temp - (ele/100) * 0.6
    return temp

if __name__ == '__main__':
    print get_season_init_temp(70, 12)
    print get_season_init_temp(-37.83, 12)
    print get_temp(-37.83, 12, 41.81)


