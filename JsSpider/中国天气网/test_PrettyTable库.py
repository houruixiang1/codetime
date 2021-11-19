from prettytable import PrettyTable
p = PrettyTable()
# p.add_row("shijian")
# print(p)
win = ['shijian','kongjina','ren']
p.add_column('风量', win)
city = ['中国','美国','日本']
p.add_column('祖国',city)
print(p)