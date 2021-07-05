
for i in [10,20,30,40,50,60,70,80,90,100]:
    filename = "/tmp/alberta_percentage_%d/eval_results.txt"%i
    with open(filename) as f:
        t = f.read().splitlines()[1].split("=")[1].strip()
        print(t)
