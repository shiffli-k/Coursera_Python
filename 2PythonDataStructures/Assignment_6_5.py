# Assignment 6.5
text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find("0"): len(text)]))
