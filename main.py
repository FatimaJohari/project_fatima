# -*- coding: utf-8 -*-

from forecasting.forecasting import Forecasting
import matplotlib.pyplot as plt
#directory = "C:/Users/fatjo876/Documents/Year_2/PhD Courses/AdvancedSolarIrradianceTheory-master/sxf_2015-2016.txt"

def main():
    print("Specify your solar radiation file directory")
    # summarize history for accuracy
    data = Forecasting()
    data.forecasting()
    data.display()


if __name__ == "__main__":
    main()