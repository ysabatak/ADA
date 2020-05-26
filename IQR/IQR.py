#IMPORTANT: the creditcard.csv file has to be in the same folder.

import pandas as pd
import numpy as np
import os

os.system("clear")

shuffled_dataset = pd.read_csv("creditcard.csv")

#######removing V14 outliers#######

#extracting V14 features
v14_data = shuffled_dataset['V14'].loc[shuffled_dataset['Class'] == 1].values

#calculation and printing of IQR and quartiles for V14
q25 = np.percentile(v14_data, 25)
q75 = np.percentile(v14_data, 75)
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
IQR = q75 - q25
print('IQR: {}'.format(IQR))

#Determination of boundaries limits 
v14_cutoff = IQR * 1.6
v14_q25 = q25 - v14_cutoff
v14_q75 = q75 + v14_cutoff
print('Cut Off: {}'.format(v14_cutoff))
print('\n')
print ('V14: ')
print('Lower threshold: {}'.format(v14_q25))
print('upper threshold {}'.format(v14_q75))

outliers = [x for x in v14_data if x < v14_q25 or x > v14_q75]
print('Outliers:{}'.format(outliers))
print('Number of outliers for V14: {}'.format(len(outliers)))


shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V14'] > v14_q75) | (shuffled_dataset['V14'] < v14_q25)].index)
print('='*25)



#######removing V12 outliers#######

#extracting V12 features
v12_data = shuffled_dataset['V12'].loc[shuffled_dataset['Class'] == 1].values

#calculating and printing IQR and quartiles for V12
q25 = np.percentile(v12_data, 25)
q75 = np.percentile(v12_data, 75)
IQR = q75 - q25
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
print('IQR: {}'.format(IQR))

#Determination of boundaries limits 
v12_cutoff = IQR * 1.6
v12_q25 = q25 - v12_cutoff
v12_q75 = q75 + v12_cutoff
print('Cut Off: {}'.format(v12_cutoff))
print('\n')
print ('V12: ')
print('Lower threshold: {}'.format(v12_q25))
print('Upper threshold: {}'.format(v12_q75))
outliers = [x for x in v12_data if x < v12_q25 or x > v12_q75]
#for x in v12_data:
    #if x < v12_q25 or x > v12_q75:
     #   outliers.append(x)

print('Outliers: {}'.format(outliers))
print('Number of outliers for V12: {}'.format(len(outliers)))
shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V12'] > v12_q75) | (shuffled_dataset['V12'] < v12_q25)].index)
print('='*25)



#######removing V10 outliers#######

#extracting V10 features
v10_data = shuffled_dataset['V10'].loc[shuffled_dataset['Class'] == 1].values

#calculating and printing IQR and quartiles for V10
q25 = np.percentile(v10_data, 25)
q75 = np.percentile(v10_data, 75)
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
IQR = q75 - q25
print('IQR: {}'.format(IQR))

##Determination of boundaries limits 
v10_cutoff = IQR * 1.6
v10_q25 =  q25 - v10_cutoff
v10_q75 = q75 + v10_cutoff
print('Cut Off: {}'.format(v10_cutoff))
print('\n')
print ('V10: ')
print('Lower threshold : {}'.format(v10_q25))
print('Upper threshold : {}'.format(v10_q75))
outliers = [x for x in v10_data if x < v10_q25 or x > v10_q75]
print('Outliers: {}'.format(outliers))
print('Number of outliers for V10: {}'.format(len(outliers)))
shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V10'] > v10_q75) | (shuffled_dataset['V10'] < v10_q25)].index)
print('='*25)

#######removing V4 outliers#######

#extracting V4 features
v4_data = shuffled_dataset['V4'].loc[shuffled_dataset['Class'] == 1].values

#calculating and printing IQR and quartiles for V4
q25 = np.percentile(v4_data, 25)
q75 = np.percentile(v4_data, 75)
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
IQR = q75 - q25
print('IQR: {}'.format(IQR))

#Determination of boundaries limits 
v4_cutoff = IQR * 1.6
v4_q25 =  q25 - v4_cutoff
v4_q75 = q75 + v4_cutoff
print('Cut Off: {}'.format(v4_cutoff))
print('\n')
print ('V4: ')
print('Lower threshold : {}'.format(v4_q25))
print('Upper threshold : {}'.format(v4_q75))
outliers = [x for x in v4_data if x < v4_q25 or x > v4_q75]
print('Outliers: {}'.format(outliers))
print('Number if outliers for V4: {}'.format(len(outliers)))
shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V4'] > v4_q75) | (shuffled_dataset['V4'] < v4_q25)].index)
print('='*25)

#######removing V11 outliers#######

#extracting V11 features
v11_data = shuffled_dataset['V11'].loc[shuffled_dataset['Class'] == 1].values

#calculating and printing IQR and quartiles for V11
q25 = np.percentile(v11_data, 25)
q75 = np.percentile(v11_data, 75)
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
IQR = q75 - q25
print('IQR: {}'.format(IQR))

#Determination of boundaries limits 
v11_cutoff = IQR * 1.6
v11_q25 =  q25 - v11_cutoff
v11_q75 = q75 + v11_cutoff
print('Cut Off: {}'.format(v11_cutoff))
print('\n')
print ('V11: ')
print('Lower threshold : {}'.format(v11_q25))
print('Upper threshold : {}'.format(v11_q75))
outliers = [x for x in v11_data if x < v11_q25 or x > v11_q75]
print('Outliers: {}'.format(outliers))
print('Number if outliers for V11: {}'.format(len(outliers)))
shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V11'] > v11_q75) | (shuffled_dataset['V11'] < v11_q25)].index)
print('='*25)


#######removing V10 outliers#######

#extracting V16 features
v16_data = shuffled_dataset['V16'].loc[shuffled_dataset['Class'] == 1].values

#calculating and printing IQR and quartiles for V16
q25 = np.percentile(v16_data, 25)
q75 = np.percentile(v16_data, 75)
print('Q25: {}'.format(q25))
print('Q75: {}'.format(q75))
IQR = q75 - q25
print('IQR: {}'.format(IQR))

#Determination of boundaries limits 
v16_cutoff = IQR * 1.6
v16_q25 =  q25 - v16_cutoff
v16_q75 = q75 + v16_cutoff
print('Cut Off: {}'.format(v16_cutoff))
print('\n')
print ('V16: ')
print('Lower threshold : {}'.format(v16_q25))
print('Upper threshold : {}'.format(v16_q75))
outliers = [x for x in v16_data if x < v16_q25 or x > v16_q75]
print('Outliers: {}'.format(outliers))
print('Number if outliers for V11: {}'.format(len(outliers)))
shuffled_dataset = shuffled_dataset.drop(shuffled_dataset[(shuffled_dataset['V16'] > v16_q75) | (shuffled_dataset['V16'] < v16_q25)].index)
print('='*25)
