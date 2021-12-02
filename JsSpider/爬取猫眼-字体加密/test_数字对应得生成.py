
import matplotlib.pyplot as plt
import re

str = """"
<contour>
        <pt x="372" y="719" on="1"/>
        <pt x="9" y="268" on="1"/>
        <pt x="9" y="149" on="1"/>
        <pt x="386" y="149" on="1"/>
        <pt x="386" y="0" on="1"/>
        <pt x="453" y="0" on="1"/>
        <pt x="453" y="149" on="1"/>
        <pt x="584" y="149" on="1"/>
        <pt x="584" y="268" on="1"/>
        <pt x="453" y="268" on="1"/>
        <pt x="453" y="719" on="1"/>
      </contour>
      <contour>
        <pt x="367" y="609" on="1"/>
        <pt x="386" y="609" on="1"/>
        <pt x="386" y="268" on="1"/>
        <pt x="100" y="268" on="1"/>
      </contour>
"""


x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str)]
y = [int(i) for i in re.findall(r'y="(.*?)" on=', str)]

print(x)
print(y)

plt.plot(x, y)
plt.show()