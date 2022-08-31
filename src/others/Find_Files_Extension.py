import os
import fnmatch

dir = 'C:/Local_Petrofac/media/pf-spark-shared/pf-data-model/rnn_outputs/2018-08-14'
for file in os.listdir(dir):
    #print(file)
    if fnmatch.fnmatch(file, '*.csv'):
        print(file)
