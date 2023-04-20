# empower - a flask app for power provider price comparison

This projects aim is to create a python package that can be deployed to a 
production server and be used for comparing power provider pricing
based on power usage input

## Table of content
  * [License](#license)
  * [Installation](#installation)
    * [Requirements](#requirements)
    * [Build and install](#build-and-install)
    * [Uninstall](#uninstall)


## License
For the license of the package, refer to [LICENSE](LICENSE).


### Build and install
To build the project, download the source code either with `git`:
```sh
git clone https://github.com/retorded/future-of-fintech
```
or by downloading the source code as a zip from the browser.

To build the project, move into the now cloned repository and run 
```py
python -m build
```
This will create a new folder called `dist` in which the built package will be stored.
Running either
```sh
pip install empower-*.*.*.tar.gz  
# or 
pip install empower-*.*.*-py3-none-any.whl
```
will install the packae as a python module.


### Uninstall
Simply run
```sh
pip uninstall empower
```
and the package, along with the script, will be removed.
