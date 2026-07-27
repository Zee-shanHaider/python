name = "  Zeeshan Haider  "
print(name.strip())
print(name.lower())
print(name.upper())
print(name.replace("Haider", "Ahmed"))

sentence = "Python is great for AI"
print(sentence.split(" "))
print(sentence.find("great"))
print(sentence.startswith("Python"))
print(sentence.endswith("AI"))
print(sentence.count("i"))

words = ["Python", "is", "powerful"]
print(" ".join(words))
print("-".join(words))

language = "Python"
version = 3.11
print("Language: %s, Version: %.1f" % (language, version))
print("Language: {}, Version: {}".format(language, version))
print(f"Language: {language}, Version: {version}")
print(f"{language!r} has {len(language)} characters")
print(f"{3 * 100:.2f}")
