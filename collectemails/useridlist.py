with open('users.txt', encoding='utf-8') as rf:
    with open('idlist.txt', 'w', encoding='utf-8') as wf:
       
      for row in rf:
            columns = row.rstrip().split('\t')
            wf.write(columns[1]+'\n')



