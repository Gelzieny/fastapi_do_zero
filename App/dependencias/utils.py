import re

just_numbers = lambda a: ''.join(re.findall("\d+", a))