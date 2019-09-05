import pickle


def read_data():
	with open('data.pickle', 'rb') as f:
		data = pickle.load(f)
		print(data)

read_data()