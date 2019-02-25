# i=0
for i in range(0,10):
	if  not results['results'][i]['upc']:
		name  = str(results['results'][i]['name'])
		upc  = str(results['results'][i]['upc'])
		print("Le nom du produit  : {} , UPC Is  : {}".format(name,upc))
	else:
		print("prduit sans UPC")


for i in range(0,10):
	# upc = results['results'][i]['upc']
	try:
		upc = results['results'][i]['upc']
		name = results['results'][i]['name']
		if len(results['results'][i]['upc']) == 0:
			print("Nom du produit : {}, {} has A UCP".format(name,str(upc)))
	except:
		print("Nom du produit : {} has NO UCP".format(name))
		# pass




	code = results['results'][i]['name']
	# upc = results['results'][i]['upc']
	print("Nom du produit : {}".format(code))




for i in range(100):
    key = i % 10
    if key in d:
        d[upc] += 1
    else:
        d[key] = 1