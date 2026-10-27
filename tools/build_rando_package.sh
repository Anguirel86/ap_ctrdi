#
# Package the ctrando library for release with the apworld.
# Create a lib/ctrando folder inside the world and install
# the necessary package files
#

# Submodule needs to be initialized to build the package
if git submodule status | grep "ctrando" | grep --quiet "^-"; then
    echo "ctrando submodule is not initialized"
    exit 1
fi

# Script expects to be run from the tools directory
# We could be smarter about this, but probbaly not worth the effort
if [[ ! -e "../submodules/ctrando" ]]; then
    echo "Run this script from the tools directory"
    exit 1
fi

# Create a lib folder in the apworld main directory
pushd ..
# Delete the old package if it exists
rm -r lib/
mkdir -p lib

pushd lib
# Copy the ctrando library files
cp -r ../submodules/ctrando/src/ctrando/ .
# Copy the license
cp ../submodules/ctrando/LICENSE ctrando/
# Make an __init__.py file so that python recognizes it
touch ctrando/__init__.py

popd
popd
