name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "That means he's %d cm tall" % (height * 2.54)
print "He's %d lbs heavy." %weight
print "This means he's %d kg heavy" % (weight * .4536)
print "Actually he's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# tricky line ahead
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
