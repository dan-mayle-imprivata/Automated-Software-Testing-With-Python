
# f string (Only works with new versions of python)
name = "Bob"

print(f"Hello, {name}")

# Template strings with .format()
name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)
