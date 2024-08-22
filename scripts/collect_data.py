def collect_data(input_file):
    import re
    num_re = re.compile(r"\d+")
    deg = []
    o_deg = []
    ans = []
    cycle = []
    dpu_cycle = []
    with open(input_file) as f:
        for line in f.readlines():
            if line.startswith("node"):
                data = num_re.findall(line)
                deg.append(float(data[1]))
                o_deg.append(float(data[2]))
                ans.append(float(data[3]))
                cycle.append(float(data[4]))
            elif line.startswith("DPU"):
                data = num_re.findall(line)
                dpu_cycle.append(float(data[2]))
    return deg, o_deg, ans, cycle, dpu_cycle
