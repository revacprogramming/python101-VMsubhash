text = "X-DSPAM-Confidence:    0.8475"
k=text.find("0.")
print(float(text[k:]))