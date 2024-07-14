#  _ _  _____ __ _| |_  ___ _ _ ___ 
# | ' \/ _ \ V  V / ' \/ -_) '_/ -_)
# |_||_\___/\_/\_/|_||_\___|_| \___|
# | |___  _ __| |__| |        (_) \ 
# | / / || / _` / _` |         _ | |
# |_\_\\_, \__,_\__,_|        (_)| |
#      |__/                     /_/ 
#
# Python Text Formatting
# by nowherekydd :)

# I know this might already exist out there somewhere, but this could be useful for someone out there.

def bold(text):
  return "\033[1m" + text + "\033[0m"

# Debug/test.

print(bold("This text is bold."))