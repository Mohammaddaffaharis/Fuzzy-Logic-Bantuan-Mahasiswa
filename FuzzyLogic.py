import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_excel('Mahasiswa.xls')
pengeluaran = []
penghasilan = []
for i in file.index:
    pengeluaran.append(file['Pengeluaran'][i])
    penghasilan.append(file['Penghasilan'][i])


# high,average,low
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
def klasifikasiPengeluaran(pengeluaran):
    result = []
    result.append(pengeluaranRendah(pengeluaran))
    result.append(pengeluaranStandar(pengeluaran))
    result.append(pengeluaranTinggi(pengeluaran))
    return result

#upper,middle,bottom
def penghasilanTinggi(penghasilan):
    max = 19
    min = 14
    if(penghasilan > max):
        return 1
    elif(penghasilan > min and penghasilan <= max):
        return (penghasilan - min) / (max - min)
    elif(penghasilan <= min):
        return 0
def penghasilanRendah(penghasilan):
    max = 7
    min = 3
    if(penghasilan > max):
        return 0
    elif(penghasilan > min and penghasilan <= max):
        return (max - penghasilan) / (max - min)
    elif(penghasilan <= min):
        return 1
def penghasilanStandar(penghasilan):
    max = 13.5
    min = 7.5
    maxUnCom = 17
    minUnCom = 5
    if(penghasilan <= minUnCom or penghasilan > maxUnCom):
        return 0
    elif(penghasilan > minUnCom and penghasilan <= min):
        return (penghasilan - minUnCom) / (min - minUnCom)
    elif(penghasilan > min and penghasilan <= max):
        return 1
    elif(penghasilan > max and penghasilan <= maxUnCom):
        return (maxUnCom - penghasilan) / (maxUnCom - max)
def klasifikasiPenghasilan(penghasilan):
    result = []
    result.append(penghasilanRendah(penghasilan))
    result.append(penghasilanStandar(penghasilan))
    result.append(pengeluaranStandar(penghasilan))
def printPengeluarannPenghasilan():
    x = [3, 4.5, 5, 5.5, 7.5, 8, 9, 10]
    y1 = [0, 0, 0, 0, 0, 1, 1, 1]
    y2 = [1, 1, 1, 0, 0, 0, 0, 0]
    y3 = [0, 0, 0, 1, 1, 0, 0, 0]
    plt.plot(x, y1, label='Pengeluaran Tinggi')
    plt.plot(x, y2, label='Pengeluaran Rendah')
    plt.plot(x, y3, label='Pengeluaran Standar')
    plt.title('Pengeluaran')
    plt.legend()
    plt.show()

    x = [3, 5, 7, 7.5, 13.5, 14, 17, 19]
    y1 = [0, 0, 0, 0, 0, 1, 1, 1]
    y2 = [1, 1, 1, 0, 0, 0, 0, 0]
    y3 = [0, 0, 0, 1, 1, 0, 0, 0]
    plt.plot(x, y1, label='Penghasilan Tinggi')
    plt.plot(x, y2, label='Penghasilan Rendah')
    plt.plot(x, y3, label='Penghasilan Standar')
    plt.title('Penghasilan')
    plt.legend()
    plt.show()

def fuzzyTable(fuzzy1, fuzzy2):
    if (fuzzy1 == 'bottom') and (fuzzy2 == 'low'):
        return 'considered'
    elif (fuzzy1 == 'bottom') and (fuzzy2 == 'average'):
        return 'accepted'
    elif (fuzzy1 == 'bottom') and (fuzzy2 == 'high'):
        return 'accepted'
    elif (fuzzy1 == 'middle') and (fuzzy2 == 'low'):
        return 'considered'
    elif (fuzzy1 == 'middle') and (fuzzy2 == 'average'):
        return 'considered'
    elif (fuzzy1 == 'middle') and (fuzzy2 == 'high'):
        return 'accepted'
    elif (fuzzy1 == 'upper') and (fuzzy2 == 'low'):
        return 'rejected'
    elif (fuzzy1 == 'upper') and (fuzzy2 == 'average'):
        return 'rejected'
    elif (fuzzy1 == 'upper') and (fuzzy2 == 'high'):
        return 'considered'