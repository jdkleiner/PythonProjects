# Import libraries
import matplotlib.pyplot as plt
import pandas as pd #used for plotting data
import numpy as np
import wget
import zipfile

# "http://deq1.bse.vt.edu/d.dh/om/remote/get_modelData.php?operation=11&delimiter=tab&elementid=elementid&runid=runid&startdate=1984-10-01&enddate=2005-09-30"
# "http://deq1.bse.vt.edu/om/remote/get_modelData.php?operation=11&delimiter=tab&elementid=249169&runid=6011&startdate=1984-10-01&enddate=2005-09-30"
runlog = "http://deq1.bse.vt.edu:81/data/proj3/out/runlog6011.249169.log.zip"
wget.download(runlog)

# zf = zipfile.ZipFile('C:/Users/Desktop/THEZIPFILE.zip')
# zf = zipfile.ZipFile("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip")

with zipfile.ZipFile("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip", "r") as zip_ref:
    zip_ref.extractall("C:/Users/jklei/Desktop/PythonProjects/")

ddf = pd.read_csv("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.txt")
# # print(zf)
# # if you want to see all files inside zip folder
# zipped_filenames = zf.namelist()
# print(zipped_filenames)
# now read your csv file 
# df = pd.read_csv(zf.open('intfile.csv'))
# dtt = zf.open("runlog6011.249169.txt")
# df = pd.read_csv(zf.open("runlog6011.249169.txt"))

# archive = zipfile.ZipFile("C:/Users/jklei/Desktop/PythonProjects/runlog6011.249169.log.zip", "r")
# imgdata = archive.read("runlog6011.249169.txt")
##############################################
# ddf = with open(zf.open('runlog6011.249169.txt'), "r") as filestream:

df = pd.read_csv("C:/Users/jklei/Desktop/PythonProjects/RoanokeRiverSalem_6011.csv")
# saved_column = df.column_name #you can also use df['column_name']

Qout = df.Qout #you can also use df['column_name']
print(type(Qout))

# df.quantile([0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0])



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