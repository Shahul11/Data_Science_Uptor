from datetime import datetime

ct = datetime.now()
print(ct)
print(type(ct))

format_ct = datetime.strftime(ct, "%d/%B/%d_%H:%M:%S")
print(format_ct)
print(type(format_ct))

convreted_ct = datetime.strptime(format_ct,"%d/%B/%d_%H:%M:%S" )
print(convreted_ct)
print(type(convreted_ct))