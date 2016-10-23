tabby_cat = "\tI'm tabbed in."
persian_cat = "Im split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishpies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# not sure what this means yet
while True:
        for i in ["/","-","|","\\","|"]:
            print "%s\r" % i,
