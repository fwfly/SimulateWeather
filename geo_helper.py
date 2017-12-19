'''
Geo helper is a module to analyze geoography from input bmp file by openCV
'''

import numpy as np
import cv2


ELE_PER_COLOR = 41.81 # 6900(height of Aconcagua)/165 (color on map)

class GeoHelper:

    def __init__(self):
        self.img = None
        self.img_height = 0
        self.img_width = 0


    def read_map( self, bmp_file ):
        '''
        read a bmp file and store it into memory

        :param bmp_file: file name
        :type bmp_file : string
        '''
        self.img = cv2.imread(bmp_file, 0)
        self.img_height, self.img_width = self.img.shape

        #print self.img
        #print self.img_height, self.img_width

    def get_elevation( self, lat, log ):
        '''
        map lat and log into img position and get elevation from rgb

        param lat : latitude from -90 to 90
        type lat : Int
        param log : longitude from -180 to 180
        type log : Int

        return : meters of elevation
        '''

        y = 90 - lat
        x = 180 + log
        # change it into map position
        y = int((y/180) * self.img_height)
        x = int((x/360) * self.img_width)
        return ELE_PER_COLOR * self.img[y, x]

    def get_geo_map(self):
        return self.img


if __name__ == '__main__':
    print "Test GeoHelper"
    geo = GeoHelper()
    #geo.read_map("fabkedata") # test fake data
    geo.read_map("elevation.bmp")
    print geo.get_elevation(-33.86, 151.21) # Sydney
    print geo.get_elevation(-32.39,-70.0) # Aconcagua
