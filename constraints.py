import regex as re

starstruc = re.compile('[cv]')
vowelinit = re.compile('^v')
consfinal = re.compile('c$')
complex = re.compile('cc')
hiatus = re.compile('vv')

def nViols(f,word):
    return len(f.findall(word, overlapped = True))
