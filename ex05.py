name  = 'Zed A. Shaw'
age = 35 # not a line
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
m_height = height * 2.54
m_weight = weight / 2.2 

print "Let's talk about %s" % name
print "He's %d inches tall" % height
print "He's %d pounds heavy." % weight
print "He's %d centimeters tall" % m_height
print "He's %d kilograms heavy" % m_weight
print "Actualy that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "I'm going to convert all of the previous values into the metric system"

print "If I add %d, %d, and %d I get %d." % (age, m_height, m_weight, age + m_height + m_weight)

