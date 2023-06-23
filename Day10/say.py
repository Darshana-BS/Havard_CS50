# import cowsay
# import sys

# if len(sys.argv) == 2:  #if user provides say.py Darshana Nehulkar -> project_name <user_name>
#     cowsay.cow("hello, " + sys.argv[1])
#     # cowsay.trex("hello, " + sys.argv[1])


import sys         #access to command l;ine arguments

from saying import goodbye

if len(sys.argv) ==2:
    goodbye(sys.argv[1])   