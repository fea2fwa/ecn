with open('e-users.txt', encoding='utf-8') as ef:
    with open('idlist.txt', encoding='utf-8') as tf:
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

        diff = tset - eset

        diff = list(diff)

        for item in diff:
            print(item)

