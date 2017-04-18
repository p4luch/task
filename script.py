import os
import re
import shutil
import urllib.request


class Abstract:
    def __init__(self):
        self.data = {}

    @staticmethod
    def checkint(num):
        """
            Check if num is integer. 
        """
        try:
            int(num)
            return True
        except ValueError:
            return False

    @staticmethod
    def deletefiles(fname):
        """
            Remove downloaded file. 
        """
        os.remove(fname)

    @staticmethod
    def downloadfile(url, fname):
        """
            Download file from url and save it under fname on disk. 
        """
        with urllib.request.urlopen(url) as response, open(fname, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    def makedict(self, fname, data_cols):
        """
            Parse file contents into dictionary. 
        """
        temp_dict = {}
        with open(fname, 'r') as f:
            for line in f.readlines():
                if line.strip() != '':
                    columns = line.split()
                    if self.checkint(self.removespecial(columns[0])):
                        key = int(self.removespecial(columns[data_cols[1]])) -\
                              int(self.removespecial(columns[data_cols[2]]))
                        if key not in temp_dict.keys():
                            temp_dict[abs(key)] = []
                        temp_dict[abs(key)].append(columns[data_cols[0]])
        return temp_dict

    def manager(self, url, fname, data_cols):
        """
            Manager function.
        """
        self.downloadfile(url, fname)
        self.data = self.makedict(fname, data_cols)
        self.deletefiles(fname)
        return self.data[min(self.data.keys())]

    @staticmethod
    def removespecial(num):
        """
            Remove all non number characters from num. 
        """
        return re.sub(r'[^\d]+', '', num)


class Football(Abstract):
    def __init__(self):
        super().__init__()
        self.data_cols = [1, 6, 8]
        self.fname = 'football.dat'
        self.url = 'http://codekata.com/data/04/football.dat'

    def getclub(self):
        club = super().manager(self.url, self.fname, self.data_cols)
        print("Team(s) with the smallest difference F to A: {0}".format(club))


class Weather(Abstract):
    def __init__(self):
        super().__init__()
        self.data_cols = [0, 1, 2]
        self.fname = 'weather.dat'
        self.url = 'http://codekata.com/data/04/weather.dat'

    def getweather(self):
        day = super().manager(self.url, self.fname, self.data_cols)
        print('Day(s) with the smallest temperature spread in June 2002: {0}'.format(day))


if __name__ == '__main__':
    Football().getclub()
    Weather().getweather()
