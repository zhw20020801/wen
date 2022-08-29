# Check your boundary conditions (e.g. >= 50 should be a pass, not just > 50)
# Think about efficiency and nesting; use the fewest number of if/elif
# "The Zen of Python" says, "Flat is better than nested."
# https://www.python.org/dev/peps/pep-0020/
# You want to make sure the last path is "else", not "elif" as we always want a result here,
# so there should be no final condition (if it wasn't one of the earlier possibilities,
# it must be the last thing, no need to check if it is)


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")