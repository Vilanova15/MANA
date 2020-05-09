## Introduction and Motivation ##

Interactive fiction is software that simulates environments in which players use text commands to control characters and influence the world around them. In common usage, the term refers to text adventures, a type of adventure game where the entire interface is usually "text-only". Text adventures are one of the oldest types of computer games, and they form a subset of the adventure genre. They reached their peak in popularity in the late 1970s, with the release of notable titles such as _Zork_ and _The Hitchhiker's Guide to the Galaxy_. By the 1980s parser-driven text adventure games had defined home-computer entertainment.

In recent years, as the field of game development became increasingly advanced, text adventures were produced less and less, creators beginning to favor games with cutting-edge non-textual graphics. However, text-based games have been the basis of influential genres such as adventure and role-playing video games, continuing to be written by independent developers.

Following the belief that interactive fiction has not yet become irrelevant, _MANA_ is a programming language designed to simplify the development of text adventure games. By removing the complexity of visual design, it can help introduce people to game development with ease. It can be used to integrate non-visually artistic people that wish to express their narratives through video games but are impeded by graphic details. In addition, it can provide an appealing tool for role-playing game fans to develop, test and share their creative stories.

## Language Features ##


## Syntax and Operations Guide ##


## Video Tutorial and Demonstration ##


## Sample Code ##
```
# Initial scene
init shrine_entrance as Scene (
	name = "Shrine Entrance",
	desc = "A spooky shrine looms in front of you." + \n + "A guard blocks your way."
);

# Initial scene options
init attack_guard as Option (
	name = "Attack the guard",
	desc = "You change in! No time for questions!"
);

init run_away as Option (
	name = "Run away in terror",
	desc = "You turn back and run as fast as you can."
);

init approach_guard as Option (
	name = "Approach the guard carefully",
	desc = "You cautiously approach the skeleton guard."
);

# Possible following scenes
init guard_parries as Scene (
	name = "Guard parries",
	desc = "The skeleton guard reacts with swift movements."
);

init back_at_village as Scene (
	name = "Back at village",
	desc = "You find yourself back in the village."
);

init cautious_approach as Scene (
	name = "Cautious approach",
	desc = "You silently move towards the guard." + \n + "You hide behind a corner, keeping your eyes on him."
);

# Setting scene options
add_option attack_guard to guard_parries;
add_option approach_guard to cautious_approach;
add_option run_away to back_at_village;

# Setting initial scene order
add_next_scene guard_parries to shrine_entrance;
add_next_scene cautious_approach to shrine_entrance;
add_next_scene back_at_village to shrine_entrance;

# Setting up following scene order
add_next_scene guard_parries to cautious_approach;
add_next_scene back_at_village to cautious_approach;
```


## Implementation Tools and Approach ##
### Methodology ###

### Tools and Environment ###
- **Python 3**: language used for development
- **PLY**: Python module used for lexer and parser development
- **Visual Studio Code**: programming IDE used for development
- **GitHub**: tool used for version control

## Development Team ##
- Maria D. Vilanova Garcia
- Fernando A. Agosto Quiñones
- Carlos J. Figueroa Vazquez

![MANA Logo](Logo.png)
