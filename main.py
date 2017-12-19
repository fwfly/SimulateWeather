import geo_helper
import temperature
import pressure
import humidity


GEO_MAP = "elevation.bmp"


def get_Weather(temp, humi):
    if humi > 50:
        if temp < 0:
            return "Snow"
        else:
            return "Rain"
    return "Sunny"


def output( city, lat, log, ele, time, weather, temp, hPA, humidity ):
    #  output format "Sydney|-33.86,151.21,39|2015-12-23T05:02:12Z|Rain|+12.5|1004.3|97"
    print "%s|%f,%f,%d|%s|%s|%d|%d|%d"%( city, lat, log, ele, time, weather, temp, hPA, humidity )

def main():
    # init input data

    city = "Sydney"
    lat = -33.86
    log = 151.21
    time = "2015-12-23T05:02:12Z"
    mouth = 7

    # init elevation
    geo = geo_helper.GeoHelper()
    geo.read_map("elevation.bmp")
    ele = geo.get_elevation(lat, log)

    # compute Temperature
    temp = temperature.get_temp(lat, mouth, ele)

    # compute Pressure
    hPa = pressure.get_pressure(ele)

    # compute humidity
    humi = humidity.get_humidity(lat, log, geo.get_geo_map())

    # compute weather status
    weather = get_Weather(temp, humi)

    output( city, lat, log, ele, time, weather, temp, hPa, humi)


if __name__ == '__main__':
    main()
