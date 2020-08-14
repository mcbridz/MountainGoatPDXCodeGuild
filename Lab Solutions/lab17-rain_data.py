#filename: lab17-rain_data.py
#author: Zachary McBride

import requests
import re
from datetime import datetime

month_to_num = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

class DayData():
    # def __init__(self):
    #     #empty contructor, default to now
    #     self.datetime.date = datetime.now()
    #     self.rain_total = 0
    
    def __init__(self, dt=['1', 'Jan', '1970', '0']):
        #dt[0]=day dt[1]=month dt[2]=year dt[3]=rain_total
        self.day = int(dt[0])
        self.month = dt[1]
        self.year = int(dt[2])
        self.rain_total = int(dt[3])

    def get_rain(self):
        return self.rain_total
    
    def get_date(self):
        global month_to_num
        return datetime(self.year, month_to_num[self.month], self.day)

class RainData:
    def __init__(self):
        self.data = []
        self.num_days = 0
        self.mean = 0
    
    def add_data(self, one_day_data):
        self.data.append(one_day_data)
        self.num_days += 1

    def generate_data(self, text_in):
        for line in text_in:
            # print(line)
            data = re.match(r'(\d\d)-(\w\w\w)-(\d\d\d\d)\s+(\d+)', line)
            # print(type(data))
            if data is None:
                continue
            # print(data.group(1), data.group(2), data.group(3), data.group(4))
            #group1=day group2=month group3=year group4=rain_total
            temp_data = [data.group(1), data.group(2), data.group(3), data.group(4)]
            temp_day_data = DayData(temp_data)
            self.add_data(temp_day_data)

    def calculate_mean(self):
        ...


    
#test data for request
text = """Hayden Island Rain Gage - 1740 N. Jantzen Beach Ctr.

PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
Data are the number of tips of the rain gage bucket.
Each tip is 0.01 inches of rainfall.
 [-, missing data]
Dates and times are PACIFIC STANDARD TIME.

            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
14-AUG-2020     1    0   0   0   0   0   0   0   0   0
13-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
12-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
11-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
10-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
"""
# text_request = requests.get("https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain")
# text = text_request.text

# split up by line
text_lines = text.split('\n')
# print(len(text_lines))
# print(text_lines[15])
text_lines = text_lines[text_lines.index("------------------------------------------------------------------------------------------------------------------") + 1:]
# print(text_lines[0])

# instantiate rain_data class object for accumulating data
my_rain_data = RainData()

# populate rain_data list
for line in text_lines:
    # print(line)
    data = re.match(r'(\d\d)-(\w\w\w)-(\d\d\d\d)\s+(\d+)', line)
    # print(type(data))
    if data is None:
        continue
    # print(data.group(1), data.group(2), data.group(3), data.group(4))
    #group1=day group2=month group3=year group4=rain_total
    temp_data = [data.group(1), data.group(2), data.group(3), data.group(4)]
    temp_day_data = DayData(temp_data)
    my_rain_data.add_data(temp_day_data)



# print(my_rain_data.data[0].get_date())
exit()