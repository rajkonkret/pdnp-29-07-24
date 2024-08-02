import matplotlib.pyplot as plt
import mpld3

labels = ["Jabłko", "Banany", 'Winogrona', 'Pomarańćze']
sizes = [30, 25, 20, 45]
colors = ['red', 'blue', 'purple', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, shadow=True, startangle=90, explode=(0.1, 0, 0, 0),
        autopct='%1.1f%%')

plt.title("Wykres kołowy")
plt.axis('equal')

plt.show()

mpld3.save_html(plt.gcf(), 'plot.html')

# with open('plot.html', "w") as f:
#     f.write(html_str)
