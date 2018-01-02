import sys

import geo_helper
import temperature
import pressure
import humidity


GEO_MAP = "elevation.bmp"


def get_city_list(filename):
    '''
    Read city information from file

    param filename: file name
    type filename: String

    return list of city
    '''

    # file format
    # city|lat|log|time

    city_list = []
    with open(filename) as city_file:
        read_data = city_file.readlines()
        for data in read_data:
            data = data.rstrip("\n")
            city_info = data.split("|")
            city, lat, log, city_time = city_info
            lat = float(lat)
            log = float(log)

            # get month
            time_list = city_time.split("-")
            month = time_list[1]
            month = int(month)

            city_list.append([
                city,
                lat,
                log,
                city_time,
                month
            ])
    return city_list



def get_weather(temp, humi):
    '''
    Assume raining or snow when humidity is over 50%
    If temperature is under 0, weather is snow.

    '''

    if humi > 50:
        if temp < 0:
            return "Snow"
        else:
            return "Rain"
    return "Sunny"


def output(city, lat, log, ele, time, weather, temp, h_pa, humi):
    #  output format "Sydney|-33.86,151.21,39|2015-12-23T05:02:12Z|Rain|+12.5|1004.3|97"
    print "%s|%f,%f,%d|%s|%s|%d|%d|%d"%(city, lat, log, ele, time, weather, temp, h_pa, humi)

def main(filename):
    # init input data
    city_list = get_city_list(filename)

    for city in city_list:

        city_name, lat, log, time, month = city

        # init elevation
        geo = geo_helper.GeoHelper()
        geo.read_map("elevation.bmp")
        ele = geo.get_elevation(lat, log)

        # compute Temperature
        temp = temperature.get_temp(lat, month, ele)

        # compute Pressure
        h_pa = pressure.get_pressure(ele)

        # compute humidity
        humi = humidity.get_humidity(lat, log, geo.get_geo_map())

        # compute weather status
        weather = get_weather(temp, humi)

        output(city_name, lat, log, ele, time, weather, temp, h_pa, humi)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print "\nError: No input file"
        print "Please enter cmd as below : "
        print "    " + sys.argv[0] + " <file path/name>"

    main(sys.argv[1])
