import re


with open('emails.txt', encoding='utf-8') as rf:

    domainpv = {}
    domainuser = {}
    necpattern = 'jp.nec.com'

    for row in rf:
        columns = row.rstrip().split(' ')
        email = columns[1]
        pageview = columns[2]

        emailsplit = email.split('@')
        emaildomain = emailsplit[1]
        matchNEC = re.search(necpattern, emaildomain)
        if matchNEC:
            emaildomain = necpattern

        if emaildomain in domainpv.keys():
            domainpv[emaildomain] += int(pageview)
            domainuser[emaildomain] += 1
        else:
            domainpv[emaildomain] = int(pageview)
            domainuser[emaildomain] = 1

with open('output.txt', 'w', encoding='utf-8') as wf:

    for k, v in sorted(domainpv.items(), key=lambda x: -x[1]):
        wf.write(k+';'+str(v)+'\n')

with open('output.txt', 'a', encoding='utf-8') as wf:

    wf.write('\n\n\n')
    for k, v in sorted(domainuser.items(), key=lambda x: -x[1]):
        wf.write(k+';'+str(v)+'\n')

