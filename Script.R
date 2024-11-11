library(ggplot2)
library(lubridate)
library(zoo)
library(openair)
library(rio)
library(tidyverse)
library(dplyr)

df <- import ('C:/Users/RStudios/SUMMER_DATA.csv')
df$date_time <- lubridate::mdy_hm(df$date_time)
df <- cutData(df,type='season')#creating a column for season
df =rename(df,date=date_time)
summaryPlot(df)
summaryPlot(df)
summaryPlot(df,avg.time ='month')
summaryPlot(df,avg.time ='week')
timeVariation(df,pollutant = c('pm25','pm10'))
timeVariation(df,pollutant = c('pm25','temp'))
#Assignment 
#Get 10 functional plot with the df data
# Install and load necessary libraries
summaryPlot(subset(df, select = c('date', 'pm25', 'pm10', 'temp')))

df1 <- cutData(df, type = "season")
head(df1)

windRose(df, type = "month", layout = c(4, 3),angle = 22.5, bias.corr = TRUE)
pollutionRose(df, pollutant = "pm25")
pollutionRose(df, pollutant = "pm25", type = "temp", layout = c(4, 1))
pollutionRose(df, pollutant = "pm10", statistic = "prop.mean")
#reference to real wind direction 

pollutionRose(df, "ws",  "wd", "ws1",  "wd1", grid.line = 5)
#polar frequency 
polarFreq(df,pollutant = 'pm25',type= "month")
polarFreq(df, pollutant = "pm10", type = "month",
          statistic = "mean", min.bin = 2)
percentileRose(df, pollutant = "pm10")                             

percentileRose(mydata, poll=c( "pm10", "pm25"),
               percentile = 95, method = "cpf",
               layout = c(2, 1))
results <-polarCluster(df, pollutant="pm25", n.clusters=8, cols= "Set2") 
table(results[ "cluster"]) 
timeProp(selectByDate(df, month = 1), pollutant = "PM25", avg.time = "day",
         proportion= "cluster", col = "Set2", key.position = "top",
         key.columns = 8, date.breaks = 10, ylab = " (ug/m3)") 

timePlot(selectByDate(df, month = "jan"),
         pollutant = c( "pm25", "pm10", "temp"),
         y.relation = "free")
timePlot(df, pollutant = c( "pm10",'pm25','temp'),
         avg.time = "month", lwd = 5, lty = 1,
         group = TRUE)