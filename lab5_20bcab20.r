getwd()
setwd("C:/Users/ADITHYA KRISHNAN/OneDrive/Desktop")
car1=read.csv("CarPrice_Assignment-1.csv")
View(car1)
mean(car1$carwidth)
#mean = 65.9078
#Ho: mean of carwidth is equal to 65 
#H1: mean of carwidth is not equal to 65
t.test(car1$carwidth,mu=65,alternative = "less",conf.level = 0.95)