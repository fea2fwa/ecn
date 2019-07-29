with open('threadid.txt', encoding='utf-8') as rf:
	with open('urls.txt', 'w', encoding='utf-8') as wf:
		for row in rf:
			threadid = row.rstrip()
			wf.write('https://community.emc.com/thread/'+str(threadid)+'\n')


