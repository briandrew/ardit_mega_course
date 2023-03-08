filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Prese ntati ons.txt']

for filename in filenames:
    filename = filename.replace('.', '-',1)
    filename = filename.replace(' ', '')
    print(filename)
