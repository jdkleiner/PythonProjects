# Import libraries
import matplotlib.pyplot as plt
import pandas as pd #used for plotting data
import numpy as np
import wget
import zipfile
# import os # for removing files

# download the runlog zip file
runlog = "http://deq1.bse.vt.edu:81/data/proj3/out/runlog6011.249169.log.zip"
wget.download(runlog)

# read in the runlog file contained within the zipped folder
# this is one method that works:
zf = zipfile.ZipFile("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip")
df = pd.read_csv(zf.open("runlog6011.249169.log"))
# os.remove("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip")

# this is one method that also works:
# with zipfile.ZipFile("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip", "r") as zip_ref:
#     zip_ref.extractall("C:/Users/jklei/Desktop/PythonProjects/")
# dd = pd.read_csv("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log")

# this is the most basic method that also works
# df = pd.read_csv("C:/Users/jklei/Desktop/PythonProjects/RoanokeRiverSalem_6011.csv")

Qout = df.Qout #you can also use df['column_name']
print(type(Qout))

quantiles = np.quantile(Qout, [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0])
print(quantiles)

# conn = connect(':memory:')
# pd.read_sql('SELECT month, Qout FROM df', conn)

data_jan = df[df['month'] == 1]
data_feb = df[df['month'] == 2]
data_mar = df[df['month'] == 3]
data_apr = df[df['month'] == 4]
data_may = df[df['month'] == 5]
data_jun = df[df['month'] == 6]
data_jul = df[df['month'] == 7]
data_aug = df[df['month'] == 8]
data_sep = df[df['month'] == 9]
data_oct = df[df['month'] == 10]
data_nov = df[df['month'] == 11]
data_dec = df[df['month'] == 12]

data = [data_jan.Qout, data_feb.Qout, data_mar.Qout, data_apr.Qout, data_may.Qout, data_jun.Qout,
data_jul.Qout, data_aug.Qout, data_sep.Qout, data_oct.Qout, data_nov.Qout, data_dec.Qout]
 
fig = plt.figure(figsize =(10, 7))
 
# create plot
plt.boxplot(data)

# add title
plt.title("Roanoke River (Salem): Qout by Month")

# add axis labels
plt.xlabel("Month")
plt.ylabel("Qout (cfs)")

# show plot
plt.show()