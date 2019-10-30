# foss-north static site generator

_Copyright(C) 2019 foss-north ek.för_

This is the foss-north static site generator. Since I'm tired of Ruby, I decided to drop Jekyll and look into Jinja myself. This small setup allows me to create a data driven site from YAML files and Jinja templates.

The paths are hardcoded and based on the location of the `fn-generator.py` script. The directories are:

* `_source/` - source `*.html` files. These are Jinja templates and each file results in the corresponding file being rendered to the `_output/` directory.
* `_includes/` - includeable files. These are Jinja templates included or extended from the files in the `_source/` directory.
* `_data/` - data set `*.yaml` files. These files are exposed as variables under the global `data` variable when rendering pages.
* `_assets/` - raw assets. This subtree is copied into the `_output/` directory.
* `_output/` - the `_output/` directory. This directory is created or updated by the script and can be removed.

When rendering the pages from the `_source/` directory the global variable `data` is exposed to Jinja. This variable contains the following sub-variables:

* `data.page` the name of the current page without file extension, e.g. when rendering `index.html` the variable `data.page` is set to `index`.
* `data.pages` a list of all page names without file extensions.
* `data.N`, where _N_ corresponds to a YAML file from the `_data/` directory. Each _N_ the contains the contents of the associated YAML file.
