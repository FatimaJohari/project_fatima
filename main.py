# -*- coding: utf-8 -*-

from forecasting.forecasting import Forecasting

directory = "C:/Users/fatjo876/Documents/Year_2/PhD Courses/AdvancedSolarIrradianceTheory-master/sxf_2015-2016.txt"

def main(directory):
    print("Specify your solar radiation directory")
    Forecasting.forecasting(directory)


if __name__ == "__main__":
    main(directory)
