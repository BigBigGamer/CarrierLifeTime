import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
plt.rc('text', usetex = True)
plt.rc('font', size=13, family = 'serif')
# plt.rc('text.latex',unicode=True)
plt.rc('legend', fontsize=14)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')

# Parazite = pd.read_csv('data/data2.tsv', delimiter = '\t')
# t = Parazite['t_d,mks'].tolist()
# du2 = Parazite['dU2,mV'].tolist()
# delta = np.array(du2)/100

# data1 = np.loadtxt('data/data1.tsv',delimiter='\t')
data1 = np.loadtxt('data/dat1.tsv')
size = data1.shape
U, x = [],[]

for i in range(0,size[0]):
    x.append(data1[i][0])
    U.append(data1[i][1])

# U = np.array(U)
# print(U)
# x = np.array(x)
# x = x - np.amin(x)
# ln_U =  np.log(U)
# print(ln_U)




# pp = np.polyfit(x,ln_U,1)
# print('tan(theta) = ',pp[0])
# print('intercept = ',pp[1])
# print('lifetime',1/pp[0]*( ln_U[0] -1-pp[1] ))
# pf = np.poly1d(pp)

# plt.figure(0)

# plt.plot(x,pf(x),'k--',lw = 1)
# plt.plot(x,ln_U,'.',color = 'red')
# plt.grid(which='major', linestyle='-')
# plt.grid(which='minor', linestyle='-',color = 'lightgrey')
# plt.xlabel('$x, mm$')
# plt.ylabel('$\ln U$')
# plt.minorticks_on()



data2 = np.loadtxt('data/data2.tsv')
size2 = data2.shape
t, du1,du2 = [],[],[]

for i in range(0,size2[0]):
    t.append(data2[i][0])
    du1.append(data2[i][1])
    du2.append(data2[i][2])

t = np.array(t)
du1 = np.array(du1)
du2 = np.array(du2)
du = du1/du2
lndU = np.log(du2)

pp2 = np.polyfit(t,lndU,1)
a,b,c,d,e = np.polyfit(t,lndU,1,full = True)
print(a,b,c,d,e)


print('tan(theta) = ',pp2[0])
print('lifetime = ',1/pp2[0])
print('intercept = ',pp2[1])
pf2 = np.poly1d(pp2)

plt.figure(1)
plt.plot(t,pf2(t),'k--',lw = 1)
plt.plot(t,lndU,'r.')
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle='-',color = 'lightgrey')
plt.xlabel('$t, mks$')
plt.ylabel('$\ln (\Delta U_2)$')
plt.minorticks_on()
# plt.plot([0,25],[2.71,2.71],'-')
plt.savefig('graphs/task2.png',dpi=500)
plt.show()
