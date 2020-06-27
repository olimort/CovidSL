import pandas as pd
import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as mpl

def u(t, a, b):
    u0 = 16;
    return (a*u0*np.exp(a*t))/(a+(b*u0*(np.exp(a*t)-1)))

def v(t, a, b):
    u0 = 16;
    v0 = 2;
    k0 = 0.043;
    return ( (2*k0*np.sqrt(u0))/(np.sqrt(b*(a - b*u0))) )*(np.arctan((np.sqrt(b*u0)/np.sqrt(a- b*u0))*np.exp(0.5*a*t)) - np.arctan(np.sqrt(b*u0)/np.sqrt(a - b*u0)) ) + v0;

data = pd.read_csv('../databases/covidsl-database_santaluzia.csv')
print(data.head(32)) #print(data.tail(10))
print(data.describe())
N = len(data['Data'])
D = N-12;

time = range(0,D)

_data_ = [];
_conf_ = np.empty(D);
_recp_ = np.empty(D);

y1 = np.empty(D);
y2 = np.empty(D);

f1 = np.empty(D);
f2 = np.empty(D);

g1 = [6.5e-2, 0.56e-4];
g2 = [2.4e-1, 1.5e-6];

for k in range(D):
    _data_.append(data['Data'][12+k]);
    _conf_[k] = data['Confirmados'][12+k];
    _recp_[k] = data['Recuperados'][12+k];
for i in range(D):
    y1[i] = u(i, g1[0], g1[1]);
    y2[i] = v(i, g2[0], g2[1]);

c1,cov1 = sp.curve_fit(u, time, _conf_, g1);
c2,cov2 = sp.curve_fit(v, time, _recp_, g2);

for j in range(D):
    f1[j] = u(j, c1[0], c1[1]);
    f2[j] = v(j, c2[0], c2[1]);
#############################################################
fig = mpl.figure()
palete = mpl.get_cmap('Set1')
mpl.style.use('ggplot')
mpl.plot(_data_,_conf_, '--', linewidth=2, label='Confirmados')
mpl.plot(_data_,_recp_, '--', linewidth=2, label='Recuperados')
mpl.plot(_data_,f1, linewidth=2,label='Ajuste da curva de contágio')
mpl.plot(_data_,f2, linewidth=2,label='Ajuste da curva de recuperação')
mpl.title("Modelo matemático para o contágio e recuperação do \nCOVID-19 em Santa Luzia-PB")
mpl.xticks(time,_data_,rotation='vertical')
mpl.xlabel("Data", fontsize=14)
mpl.ylabel("Acumulado", fontsize = 14)
mpl.grid(True)
mpl.legend()
mpl.show()

print("Casos esperados para a próxima semana:", u(D+7, c1[0], c1[1]))
print("Casos recuperados para a próxima semana:", v(D+7, c2[0], c2[1]))

##############################################################
#time = range(0,N)
#g1 = [6.5e-2, 0.56e-4]
#g2 = [2.4e-1, 1.5e-6]
#
#y1 = np.empty(N);
#y2 = np.empty(N);
#for i in range (N):
#    y1[i] = u(i, g1[0], g1[1])
#    y2[i] = v(i, g2[0], g2[1])
#
#c1,cov1 = sp.curve_fit(u, time, data['Confirmados'].values, g1)
#c2,cov2 = sp.curve_fit(v, time, data['Recuperados'].values, g2)
##print(c1)
#
#f1 = np.empty(N)
#f2 = np.empty(N)
#for j in range (N):
#    f1[j] = u(j, c1[0], c1[1])
#    f2[j] = v(j, c2[0], c2[1])
#
#mpl.plot(data['Data'],data['Confirmados'])
#mpl.plot(data['Data'],data['Recuperados'])
#mpl.plot(data['Data'],f1)
#mpl.plot(data['Data'],f2)
#mpl.show()
