__author__ = 'tomasduhourq'

text = "X-DSPAM-Confidence:    0.8475"
print float(text[text.find(':') + 1:].lstrip())

