import re
a = re.search(r'py[^th]?on', "pyaon")
print(a.group(0))
