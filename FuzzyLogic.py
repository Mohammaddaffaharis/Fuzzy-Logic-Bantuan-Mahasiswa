import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_excel('Mahasiswa.xls')
pengeluaran = []
penghasilan = []
for i in file.index:
    pengeluaran.append(file['Pengeluaran'][i])
    penghasilan.append(file['Penghasilan'][i])

#upper,middle,bottom
def penghasilanTinggi(penghasilan):
    max = 12
    min = 10.5
    if(penghasilan > max):
        return 1
    elif(penghasilan > min and penghasilan <= max):
        return (penghasilan - min) / (max - min)
    elif(penghasilan <= min):
        return 0
def penghasilanRendah(penghasilan):
    max = 8
    min = 6.5
    if(penghasilan > max):
        return 0
    elif(penghasilan > min and penghasilan <= max):
        return (max - penghasilan) / (max - min)
    elif(penghasilan <= min):
        return 1
def penghasilanStandar(penghasilan):
    max = 10
    min = 8.5
    maxUnCom = 11.5
    minUnCom = 7
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
    result.append(penghasilanTinggi(penghasilan))
    return result
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

# high,average,low
def pengeluaranTinggi(pengeluaran):
    max = 9
    min = 8
    if(pengeluaran > max):
        return 1
    elif(pengeluaran > min and pengeluaran <= max):
        return (pengeluaran - min) / (max - min)
    elif(pengeluaran <= min):
        return 0
def pengeluaranRendah(pengeluaran):
    max = 6
    min = 4.5
    if(pengeluaran > max):
        return 0
    elif(pengeluaran > min and pengeluaran <= max):
        return (max - pengeluaran) / (max - min)
    elif(pengeluaran <= min):
        return 1
def pengeluaranStandar(pengeluaran):
    max = 7.5
    min = 6.5
    maxUnCom = 8.5
    minUnCom = 5
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

def inferenceTable(fuzzyPenghasilan, fuzzyPengeluaran):
    upper = fuzzyPenghasilan[2]
    middle = fuzzyPenghasilan[1]
    bottom = fuzzyPenghasilan[0]
    high = fuzzyPengeluaran[2]
    average = fuzzyPengeluaran[1]
    low = fuzzyPengeluaran[0]
    arrAccepted = []
    arrConsidered = []
    arrRejected = []
    arrTable = [
        [bottom, low],
        [bottom, average],
        [bottom, high],
        [middle, low],
        [middle, average],
        [middle, high],
        [upper, low],
        [upper, average],
        [upper, high]
    ]
    tempNilai = 0
    for j in range(9):
        tempNilai = min(arrTable[j][0], arrTable[j][1])
        if (j == 1) or (j == 2) :
            arrAccepted.append(tempNilai)
        elif (j == 0) or (j == 5) :
            arrConsidered.append(tempNilai)
        elif (j == 3) or (j == 4)  or (j == 6) or (j == 7) or (j == 8):
            arrRejected.append(tempNilai)
    accepted = max(arrAccepted)
    considered = max(arrConsidered)
    rejected = max(arrRejected)

    return accepted, considered, rejected
def defuzzyfication(inference):
    accepted = inference[0]
    considered = inference[1]
    rejected = inference[2]
    return ((accepted * 100) + (considered * 60) + (rejected * 40)) / (accepted + considered + rejected)

hasilAkhir = []
for i in range(100):
    fuzzypenghasilan = klasifikasiPenghasilan(penghasilan[i])
    fuzzypengeluaran = klasifikasiPengeluaran(pengeluaran[i])
    inference = inferenceTable(fuzzypenghasilan,fuzzypengeluaran)
    #print(inference)
    defuzz = defuzzyfication(inference)
    #print(defuzz)
    hasilAkhir.append({'id': i+1,'hasil': defuzz})
srt = sorted(hasilAkhir, key=lambda x:x['hasil'],reverse=True)
arr = []
for i in range(20):
    arr.append(srt[i])
print(arr)
