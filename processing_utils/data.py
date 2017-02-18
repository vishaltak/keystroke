import pandas as pd
from sklearn.feature_extraction import FeatureHasher

def split_data(X):
	data = []
	for i in range(0, X.shape[0]):
		tempX = X.iloc[i]
		pp = [int(value) for value in tempX.pp.split()]
		pr = [int(value) for value in tempX.pr.split()]
		rp = [int(value) for value in tempX.rp.split()]
		rr = [int(value) for value in tempX.rr.split()]
		misc = [int(tempX.ppavg), int(tempX.rpavg), int(tempX.rravg), int(tempX.pravg), int(tempX.total)]
		temp_data = tuple(pp) + tuple(rp) + tuple(rr) + tuple(pr)  + tuple(misc)
		data.append(temp_data)
	data = pd.DataFrame.from_records(data)
	return data

hasher= FeatureHasher(n_features=10, input_type='dict', non_negative=True, dtype='int64')

def get_hashed_matrix(X):
	X_transformed= []
	temp_list = []
	for i in range(X.shape[0]):
		tempX = X.iloc[i]
		rc = list(tempX.release_codes.split())
		pp = list(map(int, tempX.pp.split()))
		pr = list(map(int, tempX.pr.split()))
		rp = list(map(int, tempX.rp.split()))
		rr = list(map(int, tempX.rr.split()))
		temp_dict = {}
		for j in range(0, len(rc)-1):
			index_str = 'pp.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = pp[j]

			index_str = 'rp.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = rp[j]

			index_str = 'rr.'+ rc[j+1] + '.' + rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = rr[j]

			index_str = 'pr.'+ rc[j]
			while temp_dict.get(index_str, -1) != -1:
				index_str = '_' + index_str
			temp_dict[index_str] = pr[j]

		index_str = 'pr.'+ rc[-1]
		while temp_dict.get(index_str, -1) != -1:
			index_str = '_' + index_str
		temp_dict[index_str] = pr[-1]
		temp_dict['ppavg'] = tempX.ppavg
		temp_dict['pravg'] = tempX.pravg
		temp_dict['rpavg'] = tempX.rpavg
		temp_dict['rravg'] = tempX.rravg
		temp_dict['total'] = tempX.total
		temp_list.append(temp_dict)
	X_transformed = pd.DataFrame(hasher.fit_transform(temp_list).todense())
	return X_transformed

