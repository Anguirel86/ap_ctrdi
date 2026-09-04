# Packaging a release
Instruction for how to create a release package.

## CTRando submodule
The ctrando repository is submoduled into this repo in `submodules/ctrando`. This is to create some traceability between a packaged apworld and the associated randomizer version. 

Ensure the randomizer is on the correct commit before creating a release.

## Generating AP options
If moving to a new randomizer version, run the `tools/ap_option_gen.py` script to autogenerate the apworld's `Options.py` file based on the randomizer's arg specs. This file will need to be moved into the root directory of the project.  This ensures that the randomizer and the apworld share a common set of options.

## Creating the ranodmizer library package
The randomizer needs to be installed in the Archipelago's `lib` folder in order for the apworld to see it and generate/run.  The `build_rando_package.sh` script packages up the randomizer library and license file in a zip archive that needs to be distributed with the apworld.  The zip file will be in the root directory of the apworld repo.

## Packaging the apworld
The apworld file is created through the Archipelago launcher application.  Run the `Launcher.py` from source, and select `Build APWorlds` from the menu. This will create the `ctrdi.apworld` file.

This apworld and release library together form a release.
