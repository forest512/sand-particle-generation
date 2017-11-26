#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:43:04 2017

@author: forest
"""

# Generate the particle size which has a log-normal distribution with mean value (ln(d50)) and standard deviation sigma(ln((d85/d16)**0.5))
import numpy as np
import matplotlib.pyplot as plt

#input the mean value and the standard deviation.
d50 = [40,25,10]
Ratio = [5,10,30]
Np = 1000
mu = np.log(np.array(d50))  
sigma = np.log(np.array(Ratio)**0.5)

dp_serials =([[],[],[]]) 

for index in range(3):
    dp = []
    for i in range(Np):
        dp_temp = np.random.lognormal(mu[index],sigma[index])
        while dp_temp > 80 or dp_temp < 6:
            dp_temp = np.random.lognormal(mu[index],sigma[index])
            
        dp.append(dp_temp)
    dp_serials[index] = dp
    
dp_array = np.array(dp_serials)

# plot the histogram of the samples, along with the 
#count,bins,ignored = plt.hist(dp_array,100,normed=True, align='mid') 

#==============================================================================
# -----------plot the PDF(probability density function)--------------#
# 
# sigma = np.std(np.log(b))  
# mu = np.mean(np.log(b)) # b is an array, log(b) means excuate the log of every b.element.
# x = np.linspace(min(bins), max(bins), 10000)
# pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
#         / (x * sigma * np.sqrt(2 * np.pi)))
# plt.plot(x,pdf,color = 'r', linewidth=2)
# plt.show() 
# 
# x_space = np.linspace(min(dp_array),max(dp_array),100)
# x_space_sort = (np.sort(x_space))   #argsort would output the argument of the sort.
#==============================================================================

#-----------plot the CDF(cumulative distribution function)-----------#
for index in range(len(d50)):
# evaluate the histogram
    values, base = np.histogram(dp_array[index,:], bins=1000)
#evaluate the cumulative
    cumulative = np.cumsum(values)/dp_array[index,:].size
# plot the cumulative function
# plt.plot(base[:-1], cumulative, c='blue')
#plot the survival functionn in semilogx coordinate
    plt.semilogx(base[:-1], 1-cumulative)
    
    j, k, m= 0, 0, 0
    
    for i in range(cumulative.size):
        if cumulative[i]< 0.16:
            j=j+1
        if cumulative[i]< 0.84:
            k=k+1
        if cumulative[i]< 0.5:
            m=m+1       
#    print(j,k,m)
#    print(base[j],base[k],base[m]) # represents the d84, d16, d50.
    print('Check the characteritic size of particles after cutting off:')
    print('The d50 is',base[m])
    print('The ratio(d84/d16) after the log-normal distribution is',base[k]/base[j])
    
#==============================================================================
#     # demonstrate the size of particle whether still has a log-normal distribution after limiting the minimum and maximum size of particles.
#     print('')
#     print('The value of sigma, which equals to the ln(sqrt(d84/d16), is',np.log((base[k]/base[j])**0.5))
#     print('Check sigma by std function of the list of the particle size',np.std(np.log(dp_array)))
#     print('')
#     print('The value of mu, equals to ln(d50) is',np.log(base[m]))
#     print('The mean value of particle size calculated by mean function is',np.mean(np.log(dp_array)))
#     The results show that after limitting the range of the particle size, the particle size still has a log-normal distribution. 
#     The mean value equals to the ln(d50), and the standard ratio equals to the ln(sqrt(d84/d16)).
#     What worth paying attention is that the d50 and the standard ratio is no longer equal to the input value. They have changed and the value of them are printed in the screen.
#==============================================================================
    
plt.show()
    
## plot the cumulative function in loglog coordinate.
#plt.loglog(base[:-1], cumulative)
##plot the survival function
#plt.loglog(base[:-1], 1-cumulative)
#plt.show()

