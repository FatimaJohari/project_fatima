# project_fatima

In this project I am going to improve some of my codes on solar radiation forecasting using deep neural networks.

By specifying the input solar radiation file directory, desired variable, time steps into the past and future, the solar radiation is predicted using a simple LSTM network. 

Method:
1. put the "sxf_2015-2016.txt" in your desired path
2. copy the path where the package ask for. 
3. decide on which variable you would like to get the forecasts
* 'dw_solar' can be used
4. choose how many hours into the past should be kept by the memory
5. choose how many hours into the future should be predicted

Run the package and in the end see the accuarcy of the LSTM forecast
** the epochs, layers, neurons and etc. can be modified as desired. 
