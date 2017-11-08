import util

runpath = "./data/new"
datapath = "./data/orig"
test = util.VacTHManip(datapath, runpath)

print(test.get_data_folder())
