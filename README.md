# SimulateWeather
This is a weather simulation program based on input city and time.


## Before Run program
You need to install openCV module

    pip install opencv-python
    
## Usage
Just run and output data

    python GenerateWeather.py <file name/path>
    
or you can output as a file

    python GenerateWeather.py <file name/path> > <output file>
    
## Input file format
Script think every sigle line is a city.

Format are as below

    <City name>|<latitude>|<longitude>|<time>
    
For sampe input file, please check **test_data**

## Compatibility
Python 2.7
