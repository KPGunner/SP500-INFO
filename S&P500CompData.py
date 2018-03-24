import quandl
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')


df = quandl.get("YALE/SPCOMP", authtoken="YOUR AUTH TOKEN", end_date="2018-02-23")

print(df.tail(5))

df.plot()
plt.title('S&P Composite Data')
plt.show()
