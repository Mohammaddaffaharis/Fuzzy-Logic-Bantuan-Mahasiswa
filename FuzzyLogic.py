import pandas as pd
import matplotlib.pyplot as plt

# Penghasilan (upper,middle,bottom)
def penghasilanTinggi(penghasilan):
    max = 16
    min = 12
    if(penghasilan > max):
        return 1
    elif(penghasilan > min and penghasilan <= max):
        return (penghasilan - min) / (max - min)
    elif(penghasilan <= min):
        return 0
def penghasilanRendah(penghasilan):
    max = 9.26
    min = 6
    if(penghasilan > max):
        return 0
    elif(penghasilan > min and penghasilan <= max):
        return (max - penghasilan) / (max - min)
    elif(penghasilan <= min):
        return 1
def penghasilanStandar(penghasilan):
    max = 11
    min = 8
    maxUnCom = 15
    minUnCom = 6
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

# Pengeluaran (high,average,low)
def pengeluaranTinggi(pengeluaran):
    max = 8
    min = 6
    if(pengeluaran > max):
        return 1
    elif(pengeluaran > min and pengeluaran <= max):
        return (pengeluaran - min) / (max - min)
    elif(pengeluaran <= min):
        return 0
def pengeluaranRendah(pengeluaran):
    max = 5
    min = 2
    if(pengeluaran > max):
        return 0
    elif(pengeluaran > min and pengeluaran <= max):
        return (max - pengeluaran) / (max - min)
    elif(pengeluaran <= min):
        return 1
def pengeluaranStandar(pengeluaran):
    max = 6
    min = 4
    maxUnCom = 9.26
    minUnCom = 2
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
    for j in range(9):
        nilai = min(arrTable[j][0], arrTable[j][1])
        if (j == 1) or (j == 2) :
            arrAccepted.append(nilai)
        elif (j == 0)  or (j == 5):
            arrConsidered.append(nilai)
        elif (j == 3) or (j == 4)  or (j == 6) or (j == 7) or (j == 8):
            arrRejected.append(nilai)
    accepted = max(arrAccepted)
    considered = max(arrConsidered)
    rejected = max(arrRejected)

    return accepted, considered, rejected
def defuzzification(inference):
    accepted = inference[0]
    considered = inference[1]
    rejected = inference[2]
    return ((accepted * 100) + (considered * 53.7) + (rejected * 23.48)) / (accepted + considered + rejected)

def readExcel():
    file = pd.read_excel('Mahasiswa.xls')
    pengeluaran = []
    penghasilan = []
    for i in file.index:
        pengeluaran.append(file['Pengeluaran'][i])
        penghasilan.append(file['Penghasilan'][i])
    return penghasilan,pengeluaran
def main():
    file = readExcel()
    penghasilan = file[0]
    pengeluaran = file[1]
    hasilAkhir = []
    for i in range(100):
        fuzzypenghasilan = klasifikasiPenghasilan(penghasilan[i])
        fuzzypengeluaran = klasifikasiPengeluaran(pengeluaran[i])
        inference = inferenceTable(fuzzypenghasilan, fuzzypengeluaran)
        defuzz = defuzzification(inference)
        hasilAkhir.append({'Baris': i + 2, 'Id': i + 1,'hasil': defuzz})
    srt = sorted(hasilAkhir, key=lambda x: x['hasil'], reverse=True)
    output = []
    for i in range(20):
        output.append(srt[i])
    createExcel(output)
def printGraph():
    x1 = [0,6,9.26,20]
    y1 = [1,1,0,0]
    x2 = [0,6,8,11,15,20]
    y2 = [0,0,1,1,0,0]
    x3 = [0,12,16,20]
    y3 = [0,0, 1,1]
    x4 = [0, 6, 8, 20]
    y4 = [0, 0, 1, 1]
    x5 = [0, 2, 5, 20]
    y5 = [1, 1, 0, 0]
    x6 = [0, 2, 4, 6, 9.26, 20]
    y6 = [0, 0, 1, 1, 0, 0]

    plt.plot(x1, y1, label='Penghasilan Rendah')
    plt.plot(x2, y2, label='Penghasilan Standar')
    plt.plot(x3, y3, label='Penghasilan Tinggi')
    plt.plot(x4, y4, label='Pengeluaran Tinggi')
    plt.plot(x5, y5, label='Pengeluaran Rendah')
    plt.plot(x6, y6, label='Pengeluaran Standar')
    #plt.axvline(x=23.48, color='red', label='Rejected')
    #plt.axvline(x=53.7, color='yellow', label='Considered')
    #plt.axvline(x=100, color='green', label='Accepted')
    plt.title('Penghasilan dan Pengeluaran')
    plt.legend()
    plt.show()
def createExcel(data):
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('Bantuan.xls')
    df.to_excel(writer, sheet_name = 'Sheet1')
    writer.save()
printGraph()
main()