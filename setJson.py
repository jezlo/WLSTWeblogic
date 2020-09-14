import json

dsName = 'SoaDS'
max = 100


ds = {}
ds[dsName] = []

data = {}
data['dataSources'] = []

data['dataSources'].append({
	
	ds[dsName].append({
		'max': max
	})
	
	
})


with open('archivJson.txt','w') as outfile:
	json.dump(data, outfile,  indent=4)