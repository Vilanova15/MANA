<head><link rel="shortcut icon" type="image/png" href="Logo.png"></head>
 
## Download MANA  

[MANA](https://github.com/Vilanova15/MANA/archive/master.zip "Download MANA")

## Dependencies

[Python 3](https://www.python.org/downloads/)  
[PLY](https://pypi.org/project/ply/)

## Introduction and Motivation

Interactive fiction is software that simulates environments in which players use text commands to control characters and influence the world around them. In common usage, the term refers to text adventures, a type of adventure game where the entire interface is usually "text-only". Text adventures are one of the oldest types of computer games, and they form a subset of the adventure genre. They reached their peak in popularity in the late 1970s, with the release of notable titles such as _Zork_ and _The Hitchhiker's Guide to the Galaxy_. By the 1980s parser-driven text adventure games had defined home-computer entertainment.

In recent years, as the field of game development became increasingly advanced, text adventures were produced less and less, creators beginning to favor games with cutting-edge non-textual graphics. However, text-based games have been the basis of influential genres such as adventure and role-playing video games, continuing to be written by independent developers.

Following the belief that interactive fiction has not yet become irrelevant, **MANA** is a programming language designed to simplify the development of text adventure games. By removing the complexity of visual design, it can help introduce people to game development with ease. It can be used to integrate non-visually artistic people that wish to express their narratives through video games but are impeded by graphic details. In addition, it can provide an appealing tool for role-playing game fans to develop, test and share their creative stories.

## Language Features
MANA is a programming language whose purpose is to automate and simplify the development of text adventure games.  

Its features include:
- Creating personalized scenes and options (actions), using “plug and play” native functions
- Variable definition
- String concatenation and newline insertion
- Object\-oriented approach
- Simplifying tree implementation for story decisions and paths
- Text\-file and command\-line (debug) interfaces
- Ease of game execution (using the terminal)

## Syntax and Operations Guide
**MANA provides the following basic functionalities:**

### Create a Scene
```
init shrine_entrance as Scene (
	name = "Shrine Entrance",
	desc = "A spooky shrine looms in front of you." + \n + "A guard blocks your way."
);
```
The _init/as_ command can initialize a _Scene_ object and store it under the given reference name. The _Scene_ object takes two string parameters: a name and a description.  
The string value for an attribute can be formed by a single string, or by the concatenation of multiple strings. The newline token `\n` inserts a newline between two strings. 

### Create an Option
```
init attack_guard as Option (
	name = "Attack the guard",
	desc = "You change in! No time for questions!"
);
```
The _init/as_ statement can initialize an _Option_ object and store it under the given reference name. The _Option_ object takes two string parameters: a name and a description.  
Like the _Scene_ object, its attributes support string concatenation and newline insertion.

### Variable definition and usage
```
var d1 = "You change in! No time for questions!";

init attack_guard as Option (
	name = "Attack the guard",
	desc = d1
);
```
The _var_ command specifies variable definition, which stores a given string value under the given reference name.  
A variable can substitute literal strings in attribute declarations.

### Set scene's trigger option
```
init guard_parries as Scene (
	name = "Guard parries",
	desc = "The skeleton guard reacts with swift movements."
);

add_option attack_guard to guard_parries;
```
_Scene_ objects contain an internal _option_ attribute, which refers to the user choice that triggers the scene (also called "trigger option").   
The _add\_option_ function sets the given _Option_ (first ID) as the trigger option for the given _Scene_ (second ID).

### Add a possible following scene to a parent scene
```
add_next_scene guard_parries to shrine_entrance;
```
_Scene_ objects also contain an internal _next\_scenes_ attribute, which stores references to all the possible following scenes it can move to.  
The _add\_next\_scene_ function adds the given child _Scene_ (first ID) to the given parent _Scene_ (second ID).  


**In addition, MANA provides some functionalities more specialized toward command-line usage:**

### Modify an object
```
modify guard_parries (
	name = "Guard parries",
	desc = "The guard draws his sword and blocks your attack."
);
```
The _modify_ function updates the referenced object's attributes.

### Display a scene or option's details
```
display_scene shrine_entrance;
display_option attack_guard;
```
The _display\_scene_ function displays a scene's details in the terminal: name, description, trigger option and next scenes.  
The _display\_option_ function displays an option's details in the terminal: name and description.

## Video Commercial/Tutorial
<iframe width="560" height="315" src="https://www.youtube.com/embed/wJb_Sb665S0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Video Demonstration

## Sample Code
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

## How to Run MANA Code
To run a game in MANA:
- Write the code in a text file.
- In the terminal, move to the MANA project directory.
- Run the MANA main script, passing the filename or the path to the file as an argument.
	- More specifically: `python MANA.py filename.txt` or `python MANA.py /path/to/file`.
	- To exit a game prematurely, press `CTRL+C`.
	
## How to Debug MANA Code
To debug code in MANA:
- In the terminal, move to the MANA project directory.
- Run the MANA\_CL script, by writing `python MANA_CL.py`. This will open the command\-line interface.
	- While in this mode, you can write lines of code to test and debug your game.
	- To exit this mode, write `quit;`.
	- Once your code has been tested, you can run your game by following the steps in the previous section.

## Implementation Tools and Approach
### Modules and Classes
The external library used for language development is PLY, which contains the Yacc and Lex modules that are used as the base for the implementation of the parser and lexer.  

The intermediate code is built using custom modules and classes. The _scene_ module contains the _Scene_ and _Option_ classes, used to create and manipulate scenes and options. The _game\_engine_ module contains the _GameEngine_ class, which is used to run written games (by traversing the scene tree), including loading and game over screens. Lastly, the _banner_ module contains functions to print ASCII art, which are used to generate the loading and game over screens.  

### Methodology
The parser includes two global variables: a reference log dictionary (for storing initialized variables and objects) and an initial scene (for storing a reference to the root of the scene tree). The _Scene_ and _Option_ classes are called and used for creating, modifying and displaying instances, as well as building the scene tree. Once the code is parsed and set up, the _GameEngine_ class is called to run the game.  

The game engine runs the game recursively from the root scene, checking for possible following scenes, outputting the option list and asking for user input. The user chooses the action to take and the engine moves to the following scene. If it reaches a dead end, the engine ends the game with a game over screen.

### Tools and Environment
- **Python 3**: programming language used for development.
- **PLY**: Python library used for lexer and parser development.
- **Visual Studio Code**: programming IDE used for development.
- **GitHub**: web-based tool used for version control.

## Development Team
María D. Vilanova García  
Fernando A. Agosto Quiñones  
Carlos J. Figueroa Vázquez  

![MANA Logo](Logo.png)
