with open('redi.txt', encoding='utf-8') as ef:
    with open('ann.txt', encoding='utf-8') as tf:
        enames=[]
        tnames=[]
        for row in ef:
            ename = row.rstrip()
            enames.append(ename)

        for row in tf:
            tname = row.rstrip()
            tnames.append(tname)


        eset = set(enames)
        tset = set(tnames)

        diff = eset - tset

        diff = list(diff)

        for item in diff:
            print(item)
