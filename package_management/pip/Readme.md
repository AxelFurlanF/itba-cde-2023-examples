# to install a package
make install PACKAGE=numpy

# to install specific version of a package
make install-version PACKAGE=numpy VERSION=1.19.2

# to install all packages from requirements.txt
make install-all

# to upgrade a package
make upgrade PACKAGE=numpy

# to uninstall a package
make uninstall PACKAGE=numpy

# to list all packages
make list

# to show info for a specific package
make show PACKAGE=numpy

# to check all packages
make check
