# empower - a flask app for power provider price comparison

This projects aim is to create a python package that can be deployed to a 
production server and be used for comparing power provider pricing
based on power usage input

Want to know more? Keep up with the development with the dedicated trello board!
[Trello board](https://trello.com/invite/b/05b6QJpn/ATTIb4c521403918a7d8d30e2f71dbb7a1a46A4900F9/empower)

View the mindmap created at the start of the project
[Mindmap](https://atlas.mindmup.com/2023/04/6a85d050e00b11eda5ea1b2a97c72641/empower_mindmap/index.html)


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
will install the package as a python module.

To initialize the database
```sh
flask --app empower init-db
```

Then run the app with flask
```sh
flask --app empower run
```

### Uninstall
Simply run
```sh
pip uninstall empower
```
and the package, along with the script, will be removed.
