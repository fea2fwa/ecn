with open('users.txt', encoding='utf-8') as rf:
    with open('namelist4SQL.txt', 'w', encoding='utf-8') as wf:
        i=0
        for row in rf:
            columns = row.rstrip().split('\t')
            if i==0:
                wf.write('username ='+'\''+columns[1]+'\'\n')
                i=1
            else:
                wf.write('or username ='+'\''+columns[1]+'\'\n')


