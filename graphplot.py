import numpy as np
import matplotlib.pyplot as plt
def plotsent(pos, neg, neu, title):
    lst = ['Positive' , 'Negative', 'Neutral']
    sentiment = list()
    sentiment.append(pos)
    sentiment.append(neg)
    sentiment.append(neu)
    y_pos = np.arange(len(lst))
    plt.title(title)
    plt.bar(y_pos, sentiment)
    plt.xticks(y_pos, lst)
    plt.show()

#plotsent(200, 10, 150, 'Tripura')
