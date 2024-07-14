id_dict = {}

# Exceedingly simple ID generation :D
def generateID(purpose):
    id_dict[purpose] = id_dict.get(purpose, 0) + 1
    return id_dict[purpose]
