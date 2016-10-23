es01 = "\\"
es02 = "\'"
es03 = "\""
es04 = "\a"
es05 = "\b"
es06 = "\f"
es07 = "\n"
# es08 = "\N{name}"
es09 = "\r"
es10 = "\t"
# es11 = "\uxxxx"
# es12 = "\uxxxxxxxx"
es13 = "\v"
# es14 = "\ooo"
# es15 = "\vhh"

n01 = "Backslash"
n02 = "Single Quote"
n03 = "Double Quote"
n04 = "ASCII Bell (BEL)"
n05 = "ASCII backspace (BS)"
n06 = "ASCII formfeed (FF)"
n07 = "ASCII linefeed (LF)"
n08 = "Unicode Character"
n09 = "Carriage Return (CR)"
n10 = "Horizontal Tab (TAB)"
n11 = "16-bit Hex Value Character"
n12 = "32-bit Hex Value Character"
n13 = "ASCII vertical tab (VT)"
n14 = "Octal Value Character"
n15 = "hh Hex Value Character"

value = """%r"""
name = "This is the %s escape sequence. "
# description = "This creates %s"
example = "This %s is an example of the escape sequence in action."


print value % es01 + "\t" + name % n01 + example % es01
print value % es02 + "\t" + name % n02 + example % es02
print value % es03 + "\t" + name % n03 + example % es03
print value % es04 + "\t" + name % n04 + example % es04
print value % es05 + "\t" + name % n05 + example % es05
print value % es06 + "\t" + name % n06 + example % es06
print value % es07 + "\t" + name % n07 + example % es07
# print value % es08 + "\t" + name % n08 + example % es08
print value % es09 + "\t" + name % n09 + example % es09
print value % es10 + "\t" + name % n10 + example % es10
# print "%r % es11 + "\t" + name % n11 + example % es11
# print value % es12 + "\t" + name % n12 + example % es12
print value % es13 + "\t" + name % n13 + example % es13
# print "%r % es14 + "\t" + name % n14 + example % es14
# print "%r % es15 + "\t" + name % n15 + example % es15
