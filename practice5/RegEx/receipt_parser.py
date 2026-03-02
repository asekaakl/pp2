#ex1
import re

pattern = r"^ab*$"

test = ["a", "ab", "abb", "ac"]
for t in test:
    print(t, bool(re.match(pattern, t)))
#ex2
import re

pattern = r"^ab{2,3}$"

test = ["abb", "abbb", "ab", "abbbb"]
for t in test:
    print(t, bool(re.match(pattern, t)))
#ex3
import re

text = "hello_world test_string Example_Text"

pattern = r"\b[a-z]+_[a-z]+\b"

print(re.findall(pattern, text))
#ex4
import re

text = "Hello world Test Python A Bc"

pattern = r"\b[A-Z][a-z]+\b"

print(re.findall(pattern, text))
#ex5
import re

pattern = r"^a.*b$"

test = ["ab", "axxb", "a123b", "ac"]
for t in test:
    print(t, bool(re.match(pattern, t)))
#ex6
import re

text = "Hello, world. Python is fun"
result = re.sub(r"[ ,\.]", ":", text)

print(result)
#ex7
import re

text = "hello_world_example"

result = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(result)
#ex8
import re

text = "SplitThisStringAtUppercase"

result = re.findall(r"[A-Z][^A-Z]*", text)

print(result)
#ex9
import re

text = "InsertSpacesBeforeCapitals"

result = re.sub(r"([A-Z])", r" \1", text).strip()

print(result)
#ex10
import re

text = "camelCaseStringExample"

result = re.sub(r"([A-Z])", r"_\1", text).lower()

print(result)