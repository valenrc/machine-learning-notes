# predict house price usign regression
# dataset: House Sales in King County, USA

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

# cargamos los datos de kc_house_data.csv
data = np.genfromtxt('kc_house_data.csv', delimiter=',', skip_header=1)