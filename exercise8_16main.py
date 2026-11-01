import exercise8_16greetings
exercise8_16greetings.greet_user("kila")

from exercise8_16greetings import greet_user
greet_user("kila")

from exercise8_16greetings import greet_user as greet
greet("kila")

import exercise8_16greetings as greetings
greetings.greet_user("kila")

from exercise8_16greetings import *
greet_user("kila")