# Install and load necessary libraries
library(ggplot2)
library(lubridate)
library(zoo)
library(openair)
library(rio)
library(tidyverse)
library(dplyr)

# Load the data
data <- read.csv("C:/Users/ampon/Desktop/R PROGRAMMING/SUMMER_DATA.csv")
data$date_time <- lubridate::mdy_hm(data$date_time)
data <- cutData(data, type = 'season') # creating a column for season
data <- rename(data, date = date_time)

# Summary plots
summaryPlot(data)
summaryPlot(data, avg.time = 'month')
summaryPlot(data, avg.time = 'week')

# Time Variation plots
timeVariation(data, pollutant = c('pm25', 'pm10'))
timeVariation(data, pollutant = c('pm25', 'temp'))

# Assignment: Get 10 functional plots with the data
summaryPlot(subset(data, select = c('date', 'pm25', 'pm10', 'temp')))

# Creating additional plots
data1 <- cutData(data, type = "season")
head(data1)

# Wind Rose plot
windRose(data, type = "month", layout = c(4, 3), angle = 22.5, bias.corr = TRUE)

# Pollution Rose plots
pollutionRose(data, pollutant = "pm25")
pollutionRose(data, pollutant = "pm25", type = "temp", layout = c(4, 1))
pollutionRose(data, pollutant = "pm10", statistic = "prop.mean")

# Polar Frequency plots
polarFreq(data, pollutant = 'pm25', type = "month")
polarFreq(data, pollutant = "pm10", type = "month", statistic = "mean", min.bin = 2)

# Percentile Rose plot
percentileRose(data, pollutant = "pm10")
percentileRose(data, pollutant = c("pm10", "pm25"), percentile = 95, method = "cpf", layout = c(2, 1))

# Polar Cluster plot
results <- polarCluster(data, pollutant = "pm25", n.clusters = 8, cols = "Set2")
table(results[ "cluster"])

# TimeProportion plot
timeProp(selectByDate(data, month = 1), pollutant = "pm25", avg.time = "day", proportion = "cluster",
         col = "Set2", key.position = "top", key.columns = 8, date.breaks = 10, ylab = "(ug/m3)")

# TimePlot with specific month
timePlot(selectByDate(data, month = "jan"), pollutant = c("pm25", "pm10", "temp"), y.relation = "free")

# Monthly average TimePlot
timePlot(data, pollutant = c("pm10", "pm25", "temp"), avg.time = "month", lwd = 5, lty = 1, group = TRUE)
