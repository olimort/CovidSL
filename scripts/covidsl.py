import csv
import matplotlib.pyplot as mpl

f   = open('../databases/covidsl-database_santaluzia.csv', 'r')
d   = csv.DictReader(f)
dt  = []

data = []
conf = []
recp = []
obit = []

for row in d:
    dt.append(row)

for i in range(0,len(dt)):
    data.append(dt[i]['Data'])
    conf.append(int(dt[i]['Confirmados']))
    recp.append(int(dt[i]['Recuperados']))
    obit.append(int(dt[i]['Obitos']))

time = range(0,len(data))
fig = mpl.figure()
palete = mpl.get_cmap('Set1')
mpl.style.use('ggplot')
#mpl.style.use('seaborn-darkgrid')
mpl.plot(time, conf, marker='o', markersize='4', color=palete(1), linewidth=2, label='Confirmados', )
mpl.plot(time, recp, marker='o', markersize='4', color=palete(2), linewidth=2, label='Recuperados')
mpl.plot(time, obit, marker='o', markersize='4', color=palete(6), linewidth=2, label='Óbitos')
##mpl.xticks(time,data,rotation='vertical')
mpl.legend()
#mpl.ylim(0,80);
#mpl.xlim(0,30);
mpl.title("Acumulado COVID-19 em Santa Luzia-PB")
mpl.xlabel("Data", fontsize=14)
mpl.xticks(time,data,rotation='vertical')
mpl.ylabel("Acumulado", fontsize = 14)
mpl.grid(True)
mpl.show()

