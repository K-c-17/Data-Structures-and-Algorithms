#  List comprehensions
prev_list=[1,2,3,4]
new_list=[x**2 for x in prev_list]
#print(new_list)


language='Python'
alphabet_collector=[a for a in language]
#print(alphabet_collector)

prev_list1=[-1,2,-10,34,-90,234,-223,0]
neg_squares=[x**2 for x in prev_list1 if x<0]
#print(neg_squares)

upd_list=[x if x>0 else 0 for x in prev_list1]
#print(upd_list)


