with open('PEPortal_Users.txt', encoding='utf-8') as rf:
    with open('e-users.txt', 'w', encoding='utf-8') as wf:
        for row in rf:
            columns = row.rstrip().split('\t')
            username = columns[1]
            wf.write(username+'\n')

 
