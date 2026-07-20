# Dev setup:

## One time setup and installs
### Clone the Archipelago repo:
  - `git clone https://github.com/ArchipelagoMW/Archipelago.git`

### Clone this (CT RDI) repo:
Either clone it into the archipelado worlds directory, or clone it elsewhere and link it in
  - `git clone https://github.com/Anguirel86/apctrdi.git`
  - `ln -sf apctrdi Archipelago/worlds/ctrdi`

### Clone the ctrando repo:
NOTE: The multiworld updates arent in the main repo yet
  - `git clone -b multiworld https://github.com/Anguirel86/ctrando.git`

### Set up a virtual environment and install the rando (sub in python version as appropriate)
  - `python3.12 -m venv venv`
  - `source venv/bin/activate`
  - `pip install ctrando/`

### Run the Archipelago launcher.
This will also install a bunch of dependencies, so make sure you're in your venv
  - `cd Archipelago`
  - `python Launcher.py`

## Regenerating options
The ctrdi Options.py is generated from the ctrando arg specs.  Run the `tools/ap_option_gen.py` script and copy the file into the ctrdi base directory.

Run the launcher and select `Generate Template Options` to create new yaml template files

## Generating a game
In order to generate a game, you will need a yaml file.  Generate the templates from the launcher.  They will be placed in the `Archipelado/Players/Templates` directory.

Copy the RDI template one directory up to the Players directory.  Change settings as desired.

Go back to the launcher window and select `Generate`.  A new terminal will pop up with generate status.
