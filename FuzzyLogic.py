import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_excel('Mahasiswa.xls')
pengeluaran = []
penghasilan = []
for i in file.index:
    pengeluaran.append(file['Pengeluaran'][i])
    penghasilan.append(file['Penghasilan'][i])

def pengeluaranTinggi(pengeluaran):
    max = 10
    min = 8
    if(pengeluaran > max):
        return 1
    elif(pengeluaran > min and pengeluaran <= max):
        return (pengeluaran - min) / (max - min)
    elif(pengeluaran <= min):
        return 0
def pengeluaranRendah(pengeluaran):
    max = 5
    min = 3
    if(pengeluaran > max):
        return 0
    elif(pengeluaran > min and pengeluaran <= max):
        return (max - pengeluaran) / (max - min)
    elif(pengeluaran <= min):
        return 1
def pengeluaranStandar(pengeluaran):
    max = 7.5
    min = 5.5
    maxUnCom = 9
    minUnCom = 4.5
    if(pengeluaran <= minUnCom or pengeluaran > maxUnCom):
        return 0
    elif(pengeluaran > minUnCom and pengeluaran <= min):
        return (pengeluaran-minUnCom) / (min-minUnCom)
    elif(pengeluaran > min and pengeluaran <= max):
        return 1
    elif(pengeluaran > max and pengeluaran <= maxUnCom):
        return (maxUnCom-pengeluaran) / (maxUnCom-max)
def penghasilanTinggi(penghasilan):
    max = 10
    min = 8
    if(penghasilan > max):
        return 1
    elif(penghasilan > min and penghasilan <= max):
        return (penghasilan - min) / (max - min)
    elif(penghasilan <= min):
        return 0
def penghasilanRendah(penghasilan):
    max = 5
    min = 3
    if(penghasilan > max):
        return 0
    elif(penghasilan > min and penghasilan <= max):
        return (max - penghasilan) / (max - min)
    elif(penghasilan <= min):
        return 1
def penghasilanStandar(penghasilan):
    max = 7.5
    min = 5.5
    maxUnCom = 9
    minUnCom = 4.5
    if(penghasilan <= minUnCom or penghasilan > maxUnCom):
        return 0
    elif(penghasilan > minUnCom and penghasilan <= min):
        return (penghasilan - minUnCom) / (min - minUnCom)
    elif(penghasilan > min and penghasilan <= max):
        return 1
    elif(penghasilan > max and penghasilan <= maxUnCom):
        return (maxUnCom - penghasilan) / (maxUnCom - max)

x = [3,4.5,5,5.5,7.5,8,9,10]
y1 = [0,0,0,0,0,1,1,1]
y2 = [1,1,1,0,0,0,0,0]
y3 = [0,0,0,1,1,0,0,0]

plt.plot(x, y1, label='Pengeluaran Tinggi')
plt.plot(x, y2, label='Pengeluaran Rendah')
plt.plot(x, y3, label='Pengeluaran Standar')
plt.title('Pengeluaran')
plt.legend()
plt.show()