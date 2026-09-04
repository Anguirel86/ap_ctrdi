#
# Package the ctrando library for release with the apworld.
#
# This library package contains the ctrando code and license and should be
# installed in the Archipelago lib folder.
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

pushd ../submodules/ctrando/src/ctrando
# Copy the license file here so it gets included in the package
cp ../../LICENSE .

zip -r ctrando.zip *
package_success=$?

if [ $package_success -ne 0 ]; then
    # Zip failed, clean up as best we can
    echo "Failed to create rando package"
    rm -f ctrando.zip
fi

rm LICENSE
popd

if [ $package_success -eq 0 ]; then
    # Move the package to the current working directory
    mv ../submodules/ctrando/src/ctrando/ctrando.zip .
fi
