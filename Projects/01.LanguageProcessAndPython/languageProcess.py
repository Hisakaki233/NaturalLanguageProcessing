from nltk.book import *

print(text1.concordance("monstrous"))
print("---------------------")
print(text1.similar("monstrous"))
print("---------------------")
print(text2.common_contexts(["monstrous", "very"]))
print("---------------------")

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
print("---------------------")

