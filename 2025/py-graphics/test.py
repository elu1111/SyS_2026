import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({"x":np.arange(5),"y":np.random.rand(5)})

df.plot().legend(loc='center left', bbox_to_anchor=(1, 0.5))

fname="label.png"
plt.savefig(fname, bbox_inches="tight")
plt.close("all")

