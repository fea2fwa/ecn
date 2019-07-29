with open('e-users.txt', encoding='utf-8') as f:
    emails={}
    for row in f:
        email = row.rstrip()
        if email in emails.keys():
            emails[email]+=1
        else:
            emails[email]=1

    for k,v in sorted(emails.items(), key=lambda x: x[1]):
        if v != 1:
            print(str(v)+':'+k)


        
