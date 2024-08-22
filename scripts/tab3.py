dataset_list = ['WV', 'PP', 'AP', 'YT', 'PT', 'LJ']
with open('./reproduce/tab3.csv', 'w') as f:
    f.write('Name,' + ','.join(dataset_list) + '\n')
    f.write('PimPam,')
    with open('./results/pimpam_preprocess.txt', 'r') as fin:
        lines = fin.readlines()[::5]
        lines = [float(line.strip()) for line in lines]
        lines = [str(line*1e3) for line in lines]
        f.write(','.join(lines) + '\n')
    f.write('GraphPi,')
    with open('./results/graphpi_preprocess.txt', 'r') as fin:
        lines = fin.readlines()[::5]
        lines = [float(line.strip()) for line in lines]
        lines = [str(line*1e3) for line in lines]
        f.write(','.join(lines) + '\n')
