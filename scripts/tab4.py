with open('./results/pimpam_preprocess.txt', 'r') as f:
    pimpam_preprocess = f.readlines()
    pimpam_preprocess = [float(x.strip())*1e3 for x in pimpam_preprocess]

with open('./results/pimpam_time.txt', 'r') as f:
    pimpam_time = f.readlines()
    pimpam_time = [float(x.strip())*1e3 for x in pimpam_time]

with open('./results/pimpam_model_preprocess.txt', 'r') as f:
    pimpam_model_preprocess = f.readlines()
    pimpam_model_preprocess = [float(x.strip())*1e3 for x in pimpam_model_preprocess]

with open('./results/pimpam_model_time.txt', 'r') as f:
    pimpam_model_time = f.readlines()
    pimpam_model_time = [float(x.strip())*1e3 for x in pimpam_model_time]

with open('./reproduce/tab4.csv', 'w') as f:
    f.write('Pattern,YT Cost (ms),YT Benefit (ms),PT Cost (ms),PT Benefit (ms),LJ Cost (ms),LJ Benefit (ms)\n')
    f.write('C3,')
    numbers=[]
    for i,j in zip([15, 20, 25],[0,3,6]):
        cost=pimpam_model_preprocess[j]-pimpam_preprocess[i]
        benefit=pimpam_time[i]-pimpam_model_time[j]
        numbers.append(cost)
        numbers.append(benefit)
    f.write(','.join([str(x) for x in numbers])+'\n')
    f.write('R4,')
    numbers=[]
    for i,j in zip([17, 22, 27],[1,4,7]):
        cost=pimpam_model_preprocess[j]-pimpam_preprocess[i]
        benefit=pimpam_time[i]-pimpam_model_time[j]
        numbers.append(cost)
        numbers.append(benefit)
    f.write(','.join([str(x) for x in numbers])+'\n')
    f.write('T6,')
    numbers=[]
    for i,j in zip([19, 24, 29],[2,5,8]):
        cost=pimpam_model_preprocess[j]-pimpam_preprocess[i]
        benefit=pimpam_time[i]-pimpam_model_time[j]
        numbers.append(cost)
        numbers.append(benefit)
    f.write(','.join([str(x) for x in numbers])+'\n')
