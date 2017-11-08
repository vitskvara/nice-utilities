import numpy as np
import pylab as pl

class VacTHManip:
	""" class for VacTH/NICE input/output manipulation and running """
	_input_folder = ""
	_output_folder = ""
	_data_folder = ""
	_run_folder = ""
	
	def __init__(self, data_folder_, run_folder_):
		self._data_folder = data_folder_
		self._run_folder = run_folder_
		self._input_folder = data_folder_ + "/input"
		self._output_folder = data_folder_ + "/output"
		
		data = np.zeros(5)
	
	def get_data_folder(self):
		return self._data_folder
		
def save2DArray(X, file):
	""" saves 2D numpy array with shape stored in the first line """
	shape = X.shape
	with open(file, 'w') as f:
		f.write(str(shape[0]) + '\n')
		f.write(str(shape[1]) + '\n')
		np.savetxt(f, X)
		f.close()
		
def load2DArray(file, verb = False):
	""" load array saved with previous function or differently in the same format """
	with open(file, 'r') as f:
		n = int(f.readline())
		m = int(f.readline())
		
		if verb:
			print("loading array of size %d x %d " % (n,m))
		
		X = np.loadtxt(f)
	return X

def save1DArray(X, file):
	""" saves 2D numpy array with shape stored in the first line """
	shape = X.shape
	with open(file, 'w') as f:
		f.write(str(shape[0]) + '\n')
		np.savetxt(f, X)
		f.close()
		
def load1DArray(file, verb = False):
	""" load array saved with previous function or differently in the same format """
	with open(file, 'r') as f:
		n = int(f.readline())
		
		if verb:
			print("loading array of size %d " % (n))
		
		X = np.loadtxt(f)
	return X
