# Cyberpunk: RED CLI Character Manager v0dev by James "nowherekydd" Burnham

This is a little pet/passion project that I'm currently working on to add to my Python portfolio. As of right now an executable is not on the horizon, but hopefully once I have more free time I can get to it. If you've got knowledge on Python and know how to edit, feel free to download the source code and run it on your own machine.

Senjak's RED GSheet... sheet has been a major resource for me referencing what I need to get done.
https://docs.google.com/spreadsheets/d/10j2XMfCsnLlROEFHeLCEhE6RJd4ENXOaqfCdsz6nOlo/edit?gid=510767756#gid=510767756

If you want to follow along with the character I'm using as a base:
https://docs.google.com/spreadsheets/d/1ppxQDmYei8Tu7lkZOBDWOZPvqtLRqGihsA42Y6ahZ5g/edit?usp=sharing

I would love to eventually do a GUI/character creator, but that is not on the horizon any time soon.

If you have any suggestions/comments, please feel free to let me know in any form of contact. I'm new to GitHub so I'm not quite sure how it works just yet.

# Roadmap

## Current Features
- Skill check menu divided by category
- Ability to re-roll a skill without having to redo category selection
- Debug output to check ability scores

## In Progress
- Basic character sheet [think scores, skills, and HP]

## Planned
- Advanced character sheet
- Cyber references [possibly database?]

## Known Bugs
- If you enter a non-numeric value when prompted for what category/skill you want to roll for, it will kick back either an error [ValueError: invalid literal for int() with base 10] (if in category menu) or roll with skill_modifier = 0 (if in skill menu). It's not high on my list of priorities for now.