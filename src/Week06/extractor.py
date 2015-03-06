__author__ = 'tomasduhourq'

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':') + 1
print float(text[pos:].lstrip())