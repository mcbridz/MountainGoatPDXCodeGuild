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

num_to_month = {
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

north_region = {
    0: 'Hayden Island Rain Gage',
    1: 'Shipyard Rain Gage',
    2: 'Columbia IPS Rain Gage',
    3: 'Albina Rain Gage',
    4: 'Simmons Rain Gage',
    5: 'Cascade PCC Rain Gage',
    6: 'WPCL Rain Gage',
    7: 'Astor Elementary School Rain Gage',
    8: 'Swan Island Rain Gage'
}

north_region_links = {
    'Hayden Island Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain',
    'Shipyard Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/shipyard.rain',
    'Columbia IPS Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/columbia_ips.rain',
    'Albina Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/albina.rain',
    'Simmons Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/simmons.rain',
    'Cascade PCC Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/pcc_cascade.rain',
    'WPCL Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/wpcl.rain',
    'Astor Elementary School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/astor.rain',
    'Swan Island Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/swan_island_pump.rain'
}

north_west_region = {
    0: 'Skyline School Rain Gage',
    1: 'Sauvie Island School Rain Gage',
    2: 'Yeon Rain Gage',
    3: 'Metro Learning Center Rain Gage',
    4: 'Bonny Slope BSD Rain Gage'
}

north_west_region_links = {
    'Skyline School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain',
    'Sauvie Island School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/sauvies_island.rain',
    'Yeon Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/yeon.rain',
    'Metro Learning Center Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/metro_center.rain',
    'Bonny Slope BSD Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/bonny_slope_BSD.rain'
}

north_east_region = {
    0: 'Fernwood School Rain Gage',
    1: 'Vernon School Rain Gage',
    2: 'Airport Way #2 Rain Gage',
    3: 'Mallory Rain Gage',
    4: 'Beaumont School Rain Gage',
    5: 'Post Office Rain Gage',
    6: 'Madison Rain Gage',
    7: 'Walmart Eco Roof Rain Gage',
    8: 'Swan Island Rain Gage',
    9: 'Forty-Second Avenue Rain Gage',
    10: 'Irvington Elementary School Rain Gage',
    11: 'Parkrose High School Rain Gage'
}

north_east_region_links = {
    'Fernwood School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/fernwood.rain',
    'Vernon School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/vernon.rain',
    'Airport Way #2 Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/airport_way.rain',
    'Mallory Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/mallory.rain',
    'Beaumont School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/beaumont.rain',
    'Post Office Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/post_office.rain',
    'Madison Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/madison.rain',
    'Walmart Eco Roof Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/walmart_ecoroof.rain',
    'Forty-Second Avenue Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/buffalo.rain',
    'Irvington Elementary School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/irvington.rain',
    'Parkrose High School Rain Gage': 'https://or.water.usgs.gov/non-usgs/bes/parkrose.rain'
}

available_regions = {
    0: 'North Region',
    1: 'North-west Region',
    2: 'North-east Region'
}

region_to_var = {
    'North Region': north_region,
    'North-west Region': north_west_region,
    'North-east Region': north_east_region
}

region_to_links = {
    'North Region': north_region_links,
    'North-west Region': north_west_region_links,
    'North-east Region': north_east_region_links
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
        self.sd = 0
        self.high_rain = 0
        self.high_day = datetime(1970, 1, 1)
    
    def add_data(self, one_day_data):
        self.data.append(one_day_data)
        self.num_days += 1

    def get_num_days(self):
        return self.num_days

    def generate_data(self, text_in):
        lines_of_text = text_in.split('\n')
        # text_lines = text_lines[text_lines.index("------------------------------------------------------------------------------------------------------------------") + 1:]
        lines_of_text = lines_of_text[lines_of_text.index("------------------------------------------------------------------------------------------------------------------") + 1:]
        for line in lines_of_text:
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
        total = 0
        for data in self.data:
            total += data.get_rain()
        total /= self.get_num_days()
        self.mean = round(total, 2)
    
    def get_mean(self):
        return self.mean

    def calculate_sd(self):
        total = 0
        for data in self.data:
            total += (data.get_rain() - self.get_mean())**2
        total /= self.get_num_days()
        self.sd = round(total, 6)

    def get_sd(self):
        return self.sd

    def most_rain_day(self):
        high_rain = self.data[0].get_rain()
        high_day = self.data[0].get_date()
        for day in self.data:
            if day.get_rain() > high_rain:
                high_rain = day.get_rain()
                high_day = day.get_date()
        self.high_rain = high_rain
        self.high_day = high_day

    def get_most_rain_day(self):
        return self.high_day

    def get_most_rain(self):
        return self.high_rain



    
#test data for request
# text = """Hayden Island Rain Gage - 1740 N. Jantzen Beach Ctr.

# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.

#             Daily  Hourly data -->
#    Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
# ------------------------------------------------------------------------------------------------------------------
# 14-AUG-2020     1    0   0   0   0   0   0   0   0   0
# 13-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 12-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 11-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 10-AUG-2020     1    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# """

##############################EASY DEMO CODE##############################
# text_request = requests.get("https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain")
# text = text_request.text

# # split up by line
# text_lines = text.split('\n')
# # print(len(text_lines))
# # print(text_lines[15])
# text_lines = text_lines[text_lines.index("------------------------------------------------------------------------------------------------------------------") + 1:]
# # print(text_lines[0])

# # instantiate rain_data class object for accumulating data
# my_rain_data = RainData()

# # populate rain_data list
# # for line in text_lines:
# #     # print(line)
# #     data = re.match(r'(\d\d)-(\w\w\w)-(\d\d\d\d)\s+(\d+)', line)
# #     # print(type(data))
# #     if data is None:
# #         continue
# #     # print(data.group(1), data.group(2), data.group(3), data.group(4))
# #     #group1=day group2=month group3=year group4=rain_total
# #     temp_data = [data.group(1), data.group(2), data.group(3), data.group(4)]
# #     temp_day_data = DayData(temp_data)
# #     my_rain_data.add_data(temp_day_data)

# # my_rain_data.calculate_mean()
# # print(my_rain_data.get_mean())


# # print(my_rain_data.data[0].get_date())
# # my_rain_data.generate_data(text_lines)
# # my_rain_data.calculate_mean()
# # my_rain_data.calculate_sd()

# # print(f'The mean rainfall is: {my_rain_data.get_mean()}, the variance of rainfall for a given day is: {my_rain_data.get_sd()}.')
############################END EASY DEMO CODE#################################

running = 'run'
input_var = ''
links_dict = {}
trailing_var = ''
region = ''
area = ''
while running != 'q':
    if running == 'run':
        print('Welcome to my rain data program utilizing data requests from online sources')
    if running == 'run' or running == 'c':
        print('Select from the following regions by entering its corresponding number:')
        for i in range(len(available_regions)):
            print(i + 1, available_regions[i])
        input_var = int(input()) - 1
        while input_var not in available_regions:
            input_var = int(input('Invalid entry, please try again.')) - 1
        running = 'region_selected'
    if running == 'region_selected':
        #get out the dict string from menuing
        region_var = region_to_var[available_regions[input_var]]
        region = available_regions[input_var]
        links_dict = region_to_links[available_regions[input_var]]
        trailing_var = input_var
        print(f'Select from the following stations in {available_regions[input_var]}:')
        for i in range(len(region_var)):
            print(i + 1, region_var[i])
        input_var = int(input()) - 1
        area = region_to_var[available_regions[trailing_var]][input_var]
        print(region, area)
        while input_var not in region_var:
            input_var = int(input('Invalid entry, please try again.')) - 1
        running = 'fetch'
    if running == 'fetch':
        fetch_url = links_dict[area]
        url_request = requests.get(fetch_url)
        text = url_request.text
        data_set = RainData()
        data_set.generate_data(text)
        running = 'analyze'
    if running == 'analyze':
        data_set.calculate_mean()
        data_set.calculate_sd()
        data_set.most_rain_day()
        running = 'display'
    if running == 'display':
        str_day = ''
        day = data_set.get_most_rain_day()
        str_day += str(day.day)
        str_day += ' '
        str_day += num_to_month[day.month]
        str_day += ', '
        str_day += str(day.year)
        print(f'''{area} in {region} had {str(data_set.get_mean())} average inches of rain this year,
        with a variance of {str(data_set.get_sd())} inches over the length of the data.
        The day with the most rain was {str(data_set.get_most_rain())} inches on {str_day}.
        ''')
        running = 'query'
    if running == 'query':
        if input('Would you like to search somewhere else? Press ENTER to continue, or type anything to quit. ') != '':
            running = 'q'
        else:
            running = 'c'