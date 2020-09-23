# All decimal 3 places

import numpy as np
import math as mm
x, y = np.loadtxt("results.csv", delimiter=",", usecols=(0, 1), unpack=True, skiprows=1)
x = list(x)
y = list(y)


# Function to compute mean
def mean(x):
   total=0
   mean_value=0
   try:
     for val in x:
       total=total+val
       mean_value=total/len(x)
   except:
       mean_value=0
   return (round(mean_value,3))


# Function to compute median. You cant use Python functions

c=sorted(x).copy()
def median(x):
   try:

       if len(x)%2==0:
           median_value=(c[len(x)/2]+c[(len(x)/2)-1])/2
           return round(median_value, 3)
       else:
           t=int(len(x)/2)
           median_value=(c[t])
           return round(median_value, 3)

   except:
       return 0
# Function to compute Standard deviation. You cant use Python functions
# def standard_deviation(x):
#     try:
#         sumofsquare=0
#         for data in x:
#             sumofsquare+=(data-mean(x))*(data-mean(x))
#         sumofsquare=sumofsquare/len(x)
#         standard_deviation_value=mm.sqrt(sumofsquare)
#         return round((standard_deviation_value),3)
#     except:
#         return 0

# Function to compute variance. You cant use Python functions
# def variance(x):
#    try:
#        return round(standard_deviation(x)*standard_deviation(x),3)
#    except:
#        return 0

# Function to compute RMSE. You cant use Python functions
# def rmse(x, y):
#     try:
#         diff=0
#         if len(x)!=len(y):
#             return 0
#         for z in range(len(x)):
#             diff+=(x[z]-y[z])*(x[z]-y[z])
#         rmse_value=diff/len(x)
#         rmse_value=mm.sqrt(rmse_value)
#         return round(rmse_value,3)
#     except:
#         return 0

# Function to compute mse. You cant use Python functions
# def mse(x, y):
#     try:
#         diff=0
#         if len(x)!=len(y):
#             return 0
#         for d in range(len(x)):
#             diff+=(x[d]-y[d])*((x[d]-y[d]))
#         mse_value=diff/len(x)
#         return round(mse_value,3)
#     except:
#         return 0


# Function to compute mae. You cant use Python functions
# def mae(x, y):
#     try:
#         diff = 0
#         sz=len(x)
#         if len(x)!=len(y):
#             return 0
#         for d in range(sz):
#             diff += abs(x[d] - y[d])
#         mae_value = diff / len(x)
#         return round(mae_value,3)
#     except:
#         return 0

# Function to compute NSE. You cant use Python functions
# def nse(x, y):
#     try:
#         if len(x)!=len(y):
#             return 0
#         diff1=0
#         diff2=0
#         for l in range(len(x)):
#             diff1+=(x[l]-y[l])*(x[l]-y[l])
#             diff2+=(x[l]-mean(x))*(x[l]-mean(x))
#         nse_value=1-diff1/diff2
#         return round(nse_value,3)
#     except:
#         return 0

# Function to compute Pearson correlation coefficient. You cant use Python functions
# def pcc(x, y):
#     try:
#         if len(x)!=len(y):
#             return 0
#         diff1=0
#         diff2=0
#         diff3=0
#         for i in range(len(x)):
#             diff1+=(x[i]-mean(x))*(y[i]-mean(y))
#             diff2+=(x[i]-mean(x))*(x[i]-mean(x))
#             diff3+=(y[i]-mean(y))*(y[i]-mean(y))
#         pcc_value=diff1/(mm.sqrt(diff2)*(mm.sqrt(diff3)))
#         return round(pcc_value,3)
#     except:
#         return 0

# Function to compute Skewness. You cant use Python functions
# def skewness(x):
#     try:
#         total = 0
#         mean_value = 0
#         try:
#             for val in x:
#                 total = total + val
#                 mean_value = total / len(x)
#         except:
#             mean_value = 0
#         diff=0
#         for i in x:
#             diff+=((i-mean(x))/standard_deviation(x))*((i-mean(x))/standard_deviation(x))*((i-mean(x))/standard_deviation(x))
#         diff=diff/len(x)
#         skewness_value=diff
#         return round(skewness_value,3)
#     except:
#         return  0
# def sorting(x):
#     try:
#         c = x.copy()
#         for a in range(len(x)):
#             for b in range(len(x) - 1):
#                 if (x[b] > x[b + 1]):
#                     z = x[b]
#                     x[b] = x[b + 1]
#                     x[b + 1] = z
#         sorted_list=c.copy()
#         return round(sorted_list,3)
#     except:
#         return 0

# Function to compute Kurtosis. You cant use Python functions
# def kurtosis(x):
#     try:
#         diff = 0
#         for i in x:
#             diff += ((i - mean(x)) / standard_deviation(x))*((i - mean(x)) / standard_deviation(x))*((i - mean(x)) / standard_deviation(x))*((i - mean(x)) / standard_deviation(x))
#         diff = diff / len(x)
#         kurtosis_value=diff
#         return round(kurtosis_value,3)
#     except:
#         return 0

# Function to compute sum. You cant use Python functions
# def summation(x):
#     try:
#         diff=0
#         for i in x:
#             diff+=i
#         summation_value=diff
#         return round(summation_value,3)
#     except:
#         return 0
