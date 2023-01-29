import pandas as pd
import matplotlib as plt
import numpy as np


# Initial clean done - 
#



revolution_path = (r'G:\Python\Assignment 1\A1_HR_Employee_Data.csv')

revolution_df = pd.read_csv(revolution_path, sep = ",", decimal = ".", header = 0, index_col = 0)

print(revolution_df)
print(revolution_df.info())
# print(revolution_df.info()) allows us to see columns, data types, shape
#as well as null values in columns Resigned, EducationalLevel, JobSatisfaction,
# MonthlyIncome, OverTime, and WorkLifeBalance. We will go through these further as we progress with data cleaning

print(revolution_df.columns)
print(revolution_df.dtypes)


#converting following data types from object to categories.
revolution_df['Resigned'] = revolution_df['Resigned'].astype('category')
revolution_df['BusinessTravel'] = revolution_df['BusinessTravel'].astype('category')
revolution_df['BusinessUnit'] = revolution_df['BusinessUnit'].astype('category')
revolution_df['Gender'] = revolution_df['Gender'].astype('category')
revolution_df['MaritalStatus'] = revolution_df['MaritalStatus'].astype('category')






#Converting columns with text values to uppercase
revolution_df['Resigned'] = revolution_df['Resigned'].str.upper()
revolution_df['BusinessTravel'] = revolution_df['BusinessTravel'].str.upper()
revolution_df['BusinessUnit'] = revolution_df['BusinessUnit'].str.upper()
revolution_df['OverTime'] = revolution_df['OverTime'].str.upper()
revolution_df['Gender'] = revolution_df['Gender'].str.upper()
revolution_df['MaritalStatus'] = revolution_df['MaritalStatus'].str.upper()







print(revolution_df.dtypes)



#Age - Data Cleaning - need to revisit category??
print(revolution_df['Age'].value_counts())
revolution_df['Age'] = revolution_df['Age'].str.strip()
revolution_df['Age'].replace('36a', '36', inplace = True)
print(revolution_df['Age'].value_counts())
revolution_df['Age'] = revolution_df['Age'].astype('int64')
print(revolution_df['Age'].min())
print(revolution_df['Age'].max())
print(revolution_df['Age'].mean())
print(revolution_df['Age'].median())

print(revolution_df.dtypes['Age']) #cleaned




#Resigned - Data Cleaning - "TARGET FEATURE
print(revolution_df['Resigned'].value_counts())
revolution_df['Resigned'] = revolution_df['Resigned'].str.strip()
print(revolution_df['Resigned'].value_counts())
#We can see that data labels 'N' and 'Y' have returned, we will change them
#for uniformity

revolution_df['Resigned'].replace('N', 'NO', inplace = True)
revolution_df['Resigned'].replace('Y', 'YES', inplace = True)

print(revolution_df['Resigned'].value_counts()) # Cleaned

revolution_df['Resigned'] = revolution_df['Resigned'].fillna(-1)
print(revolution_df[revolution_df['Resigned'] == -1])
#Returns employee 1215 and 5988

print(revolution_df['Resigned'].value_counts())




#Business Travel

revolution_df['BusinessTravel'] = revolution_df['BusinessTravel'].str.strip()
print(revolution_df['BusinessTravel'].value_counts())
#We see that some data labels in this column return 'TRAVELS_RARELY' 
# and 'RARELY_TRAVEL', so we change them for consistency below
revolution_df['BusinessTravel'].replace('TRAVELS_RARELY', 'TRAVEL_RARELY', inplace = True)
revolution_df['BusinessTravel'].replace('RARELY_TRAVEL', 'TRAVEL_RARELY', inplace = True)


print(revolution_df['BusinessTravel'].value_counts())

print(revolution_df['BusinessTravel'].value_counts()) #Cleaned





# Business Unit - Data Cleaning
print(revolution_df['BusinessUnit'].value_counts())
#1 value shows as female instead of sales, consulting or operations.
# Using the following code, we can determine that this employee is 9465
# who also entered their gender incorrectly as 'Sales
print(revolution_df[['BusinessUnit']][revolution_df.BusinessUnit == 'FEMALE'])
revolution_df['BusinessUnit'].replace('FEMALE' , 'SALES', inplace = True)

print(revolution_df['BusinessUnit'].value_counts()) #cleaned






# Education level - Data cleaning
print(revolution_df['EducationLevel'].value_counts())
revolution_df['EducationLevel'] = revolution_df['EducationLevel'].fillna(-1)
print(revolution_df[revolution_df['EducationLevel'] == -1])

#Shows employee ID 1215. to figure out appropriate Education Level we look
print(revolution_df['BusinessUnit'][1215]) # returns 2.91093

print('Mean of Whole Education Level: ', revolution_df.EducationLevel.mean())
print(revolution_df.groupby(['BusinessUnit'])['EducationLevel'].mean())
#Mean of 2.89 Education Level for Business Operations
print(revolution_df.groupby(['BusinessUnit'])['EducationLevel'].median())
#Median of Education Level for Business Operations, Thus we will replace NaN with 3

revolution_df.loc[1215, 'EducationLevel'] = 3
print(revolution_df['EducationLevel'][1215])

print(revolution_df['EducationLevel']) #cleaned





#Gender - Data Cleaning
print(revolution_df['Gender'].value_counts())

#ReturnsMale          882
#Female        591
#    Female      3
#      Male      2
#M               1
#MMale           1
#Sales           1
#male            1
#Name: Gender, dtype: int64

revolution_df['Gender'] = revolution_df['Gender'].str.strip()
revolution_df['Gender'].replace('M', 'MALE', inplace = True)
revolution_df['Gender'].replace('MMALE', 'MALE', inplace = True)

# Search for employee who entered Gender as 'Sales
print(revolution_df[['Gender']][revolution_df.Gender == 'SALES'])
#we find that error is be employee 9465, who is same employee who entered 
# Female as business unit - therefore we replace "Gender" Value as female
revolution_df['Gender'].replace('SALES', 'FEMALE', inplace = True)
print(revolution_df['Gender'].value_counts()) #Cleaned



#JobSatisfaction
print(revolution_df['JobSatisfaction'].value_counts())
print(revolution_df['JobSatisfaction'].median())
print(revolution_df['JobSatisfaction'].mean())

revolution_df['JobSatisfaction'] = revolution_df['JobSatisfaction'].fillna(-1)
print(revolution_df[revolution_df['JobSatisfaction'] == -1])
#Returns employee 1215

print(revolution_df['JobSatisfaction'].value_counts())





# Marital Status Data Cleaning
print(revolution_df['MaritalStatus'].value_counts())
revolution_df['MaritalStatus'] = revolution_df['MaritalStatus'].str.strip()
#change D to DIVORCED for consistency
revolution_df['MaritalStatus'].replace('D', 'DIVORCED', inplace = True)
print(revolution_df['MaritalStatus'].value_counts()) # cleaned





# Monthly Income - Data Cleaning
print(revolution_df['MonthlyIncome'].value_counts()) 
print('Minimum Monthly Income: ', revolution_df['MonthlyIncome'].min())
print('Maximum Monthly Income: ', revolution_df['MonthlyIncome'].max())
print('Mean Monthly Income: ', revolution_df['MonthlyIncome'].mean())
print('Median Monthly Income: ', revolution_df['MonthlyIncome'].median())


revolution_df['MonthlyIncome'] = revolution_df['MonthlyIncome'].fillna(-1)
no_money = (revolution_df[revolution_df['MonthlyIncome'] == -1])
print(no_money) #We see employees 6264, 5560, 1215 do not have figures for income, 


print('Mean of Monthly Income per Business unit is: \n', revolution_df.groupby(['BusinessUnit'])['MonthlyIncome'].mean())



print('Business Unit of Employee 6264', revolution_df['BusinessUnit'][6264])
#Consultant - Monthly Income Mean is  6252.437564
print('Business Unit of Employee 5560', revolution_df['BusinessUnit'][5560])
#Consultant - #Consultant - Monthly Income Mean is  6252.437564
print('Business Unit of Employee 1215', revolution_df['BusinessUnit'][1215]) 
# Business Operations - Monthly Income Mean is 6511.630769

# We can then exchange the missing values for monthly income with mean income
# values repective of BusinessUnit
revolution_df.loc[6264, 'MonthlyIncome'] = 6252.437564
print(revolution_df['MonthlyIncome'][6264])
revolution_df.loc[5560, 'MonthlyIncome'] = 6252.437564
print(revolution_df['MonthlyIncome'][5560])
revolution_df.loc[1215, 'MonthlyIncome'] = 6511.630769
print(revolution_df['MonthlyIncome'][1215])


print(revolution_df['MonthlyIncome'])



# Number of companies worked - Data cleaning
print('Minimum Number of Companies Worked: ', revolution_df['NumCompaniesWorked'].min())
print('Maximum Number of Companies Worked: ', revolution_df['NumCompaniesWorked'].max())
print('Mean Number of Companies Worked: ', revolution_df['NumCompaniesWorked'].mean())
print('Median Number of Companies Worked: ', revolution_df['NumCompaniesWorked'].median())

print(revolution_df['NumCompaniesWorked'])





# OverTime - Data Cleaning
print(revolution_df['OverTime'].value_counts()) #missing values
revolution_df['OverTime'] = revolution_df['OverTime'].fillna(-1)
print(revolution_df[revolution_df['OverTime'] == -1])
# Employees 3190, 9017, 2477 have missing data for overtime

print(revolution_df['AverageWeeklyHoursWorked'][3190]) #40 hours returned
print(revolution_df['AverageWeeklyHoursWorked'][9017]) #46 hours returned
print(revolution_df['AverageWeeklyHoursWorked'][2477]) #50 hours returned.



#Sanity check comparing data for 'OverTime' and 'Average Hours' to ensure that there aren't any instances of employees having
# worked 40 hours or less, but have also been entered as working Over Time.
revolution_OT = revolution_df['OverTime'] == 'YES'
revolution_df.loc[revolution_OT]['AverageWeeklyHoursWorked'] <= 40
overtime_check = revolution_df.loc[revolution_OT]['AverageWeeklyHoursWorked'] <= 40
print(overtime_check.value_counts())


#Now that we have the correct hours worked for each employee, and confirmed
#There aren't any logical inconsistancies with data in 'OverTime' and
#'AverageWeeklyHoursWorkedColumn' we can update the proper overtime values
#for each employee.

revolution_df.loc[3190, 'OverTime'] = 'NO'
print(revolution_df['OverTime'][3190])
revolution_df.loc[9017, 'OverTime'] = 'YES'
print(revolution_df['OverTime'][9017])
revolution_df.loc[2477, 'OverTime'] = 'YES'
print(revolution_df['OverTime'][2477])
revolution_df['OverTime'] = revolution_df['OverTime'].astype('category')
print('Clean results for Overtime data: ', revolution_df['OverTime'].value_counts())
print(revolution_df['OverTime'].shape)








# Percentage Salary Hike
print(revolution_df['PercentSalaryHike'].value_counts())
print('Min Percentage Salary Hike: ', revolution_df['PercentSalaryHike'].min())
print('Max Percentage Salary Hike: ', revolution_df['PercentSalaryHike'].max())
print('Mean Percentage Salary Hike: ', revolution_df['PercentSalaryHike'].mean())
print('Median Percentage Salary Hike: ', revolution_df['PercentSalaryHike'].median())
print(revolution_df['PercentSalaryHike'].shape) # check for completeness





# Performance Rating - Data Cleaning
print(revolution_df['PerformanceRating'].value_counts()) # looks good so far
print('Min Performance Rating: ', revolution_df['PerformanceRating'].min())
print('Max Performance Rating: ', revolution_df['PerformanceRating'].max())
print('Mean Performance Rating: ', revolution_df['PerformanceRating'].mean())
print('Median Performance Rating: ', revolution_df['PerformanceRating'].median())







# Number of Hours Worked (Average) - Data Cleaning

print(revolution_df['AverageWeeklyHoursWorked'].value_counts())
# one instance of 400 hours worked - requires more info on treatment

print(revolution_df[['AverageWeeklyHoursWorked']][revolution_df.AverageWeeklyHoursWorked == 400])
#returns employee ID3238
print(revolution_df['OverTime'][3238])
# Employee 3238 does not do over time
print(revolution_df['AverageWeeklyHoursWorked'].min())
print(revolution_df['AverageWeeklyHoursWorked'].max())
print(revolution_df['AverageWeeklyHoursWorked'].median())

#Masking outlier with 400 hours worked
revolution_df[revolution_df.AverageWeeklyHoursWorked == 400]
#Injecting Nan
revolution_df.loc[revolution_df.AverageWeeklyHoursWorked == 400, 'AverageWeeklyHoursWorked'] = np.nan
print(revolution_df[revolution_df.AverageWeeklyHoursWorked == 400])

revolution_df['AverageWeeklyHoursWorked'].fillna(revolution_df['AverageWeeklyHoursWorked'].median(axis=0), inplace = True)
#we see that 400 hours is an outlier and we replace 400 hours with 40
print(revolution_df['AverageWeeklyHoursWorked'][3238]) # correct






# Total Number of Working Years - Data Cleaning
print(revolution_df['TotalWorkingYears'].value_counts())
print('Min TotalWorkingYears: ', revolution_df['TotalWorkingYears'].min())
print('Max TotalWorkingYears: ', revolution_df['TotalWorkingYears'].max())
print('Mean TotalWorkingYears: ', revolution_df['TotalWorkingYears'].mean())
print('Median TotalWorkingYears: ', revolution_df['TotalWorkingYears'].median())



print(revolution_df['TotalWorkingYears'])





# Training Times Last Year - Data Cleaning
print(revolution_df['TrainingTimesLastYear'].value_counts())
print('Min Training Times Last Year: ', revolution_df['TrainingTimesLastYear'].min())
print('Max Training Times Last Year: ', revolution_df['TrainingTimesLastYear'].max())
print('Mean Training Times Last Year: ', revolution_df['TrainingTimesLastYear'].mean())
print('Median Training Times Last Year: ', revolution_df['TrainingTimesLastYear'].median())





# Work Life Balance - Data Cleaning - missing data
print(revolution_df['WorkLifeBalance'].value_counts())
print('Min Work Life Balance: ', revolution_df['WorkLifeBalance'].min())
print('Max Work Life Balance: ', revolution_df['WorkLifeBalance'].max())
print('Mean Work Life Balance: ', revolution_df['WorkLifeBalance'].mean())
print('Median Work Life Balance: ', revolution_df['WorkLifeBalance'].median())

revolution_df['WorkLifeBalance'] = revolution_df['WorkLifeBalance'].fillna(-1)
print(revolution_df[revolution_df['WorkLifeBalance'] == -1])
#Returns employee 1215

print(revolution_df['WorkLifeBalance'].value_counts())






# Years at company - Data Cleaning
print(revolution_df['YearsAtCompany'].value_counts())
print('Min Years At Company: ', revolution_df['YearsAtCompany'].min())
print('Max Years At Company: ', revolution_df['YearsAtCompany'].max())
print('Mean Years At Company: ', revolution_df['YearsAtCompany'].mean())
print('Median Years At Company: ', revolution_df['YearsAtCompany'].median())






# Years in Role - Data Cleaning
print(revolution_df['YearsInRole'].value_counts())
print('Min Years In Role: ', revolution_df['YearsInRole'].min())
print('Max Years In Role: ', revolution_df['YearsInRole'].max())
print('Mean Years In Role: ', revolution_df['YearsInRole'].mean())
print('Median Years In Role: ', revolution_df['YearsInRole'].median())






# Years Since last promotion - Data Cleaning
print(revolution_df['YearsSinceLastPromotion'].value_counts())
print('Min Years Since Last Promotion: ', revolution_df['YearsSinceLastPromotion'].min())
print('Max Years Since Last Promotion: ', revolution_df['YearsSinceLastPromotion'].max())
print('Mean Years Since Last Promotion: ', revolution_df['YearsSinceLastPromotion'].mean())
print('Median Years Since Last Promotion: ', revolution_df['YearsSinceLastPromotion'].median())






#Years with current manager - Data Cleaning
print(revolution_df['YearsWithCurrManager'].value_counts())
print('Min Years With Current Manager: ', revolution_df['YearsWithCurrManager'].min())
print('Max Years With Current Manager: ', revolution_df['YearsWithCurrManager'].max())
print('Mean Years With Current Manager: ', revolution_df['YearsWithCurrManager'].mean())
print('Median Years With Current Manager: ', revolution_df['YearsWithCurrManager'].median())


#converting following data types from object to categories.
revolution_df['Resigned'] = revolution_df['Resigned'].astype('category')
revolution_df['BusinessTravel'] = revolution_df['BusinessTravel'].astype('category')
revolution_df['BusinessUnit'] = revolution_df['BusinessUnit'].astype('category')
revolution_df['Gender'] = revolution_df['Gender'].astype('category')
revolution_df['MaritalStatus'] = revolution_df['MaritalStatus'].astype('category')




#Sanity Checks
#'OverTime' and 'Average Hours' to ensure that there aren't any instances of employees having
# worked 40 hours or less, but have also been entered as working Over Time.
revolution_OT = revolution_df['OverTime'] == 'YES'
revolution_df.loc[revolution_OT]['AverageWeeklyHoursWorked'] <= 40
overtime_check = revolution_df.loc[revolution_OT]['AverageWeeklyHoursWorked'] <= 40
print(overtime_check.value_counts())


#MORE SANITY CHECKS
check = (revolution_df[['Age', 'TotalWorkingYears']][revolution_df.Age < revolution_df.TotalWorkingYears])
print(check)

check2 = revolution_df[['Age', 'YearsAtCompany']][revolution_df.Age < revolution_df.YearsAtCompany]
print(check2)

check3 = revolution_df[['YearsInRole', 'YearsAtCompany']][revolution_df.YearsInRole > revolution_df.YearsAtCompany]
print(check3)

check4 = revolution_df[['YearsSinceLastPromotion', 'YearsInRole']][revolution_df.YearsSinceLastPromotion > revolution_df.YearsInRole] #returns 159 results. possibly indicates people being in similar roles but at different company
print(check4)

check5 = revolution_df[['YearsAtCompany', 'YearsInRole']][revolution_df.YearsAtCompany < revolution_df.YearsInRole]
print(check5)

check6 = revolution_df[['YearsInRole', 'YearsWithCurrManager']][revolution_df.YearsInRole > revolution_df.YearsWithCurrManager]
print(check6) #there are 432 employees who've spent more years in role than with current manager

check7= revolution_df[['YearsInRole', 'YearsWithCurrManager']][revolution_df.YearsInRole < revolution_df.YearsWithCurrManager]
print(check7) #there are 377 employees who have spent more years with current manager than years in current role.
#result of check3 and check 4 possibly due to restructures and promotions.

check8 = revolution_df[['TotalWorkingYears', 'YearsAtCompany']][revolution_df.TotalWorkingYears < revolution_df.YearsAtCompany]
print(check8) # shows employee 5560 has worked at company longer than he's actually been working.


##insights
print(revolution_df.groupby(['OverTime'])['AverageWeeklyHoursWorked'].min())
print(revolution_df.groupby(['OverTime'])['AverageWeeklyHoursWorked'].max())
print(revolution_df.loc[5560, :])


filter1 = revolution_df['OverTime']=='NO'
filter2 = revolution_df['AverageWeeklyHoursWorked']>40
print(revolution_df.where(filter1 & filter2, inplace = True))


     
        
  
