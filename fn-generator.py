#!/usr/bin/env python3
import os
import yaml
from jinja2 import Environment, FileSystemLoader
from distutils.dir_util import copy_tree

# Attempt to create output directory
try:
    os.mkdir('_output/')
except FileExistsError:
    pass

# Copy _assets into _output
copy_tree('_assets', '_output')

# Populate yaml data
print("Indexing data files...")
data = {}
for file in os.listdir('_data/'):
    if file.endswith('.yaml'):
        dataset = file[:-5]
        print("    {}".format(dataset))
        with open(os.path.join('_data/', file)) as stream:
            data[dataset] = yaml.safe_load(stream)

# Find all template pages
print("Indexing template pages...")
pages = []
for file in os.listdir('_source/'):
    if file.endswith('.html'):
        page = file[:-5]
        print("    {}".format(page))
        pages.append(page)
data['pages'] = pages

# Create jinja2 environment
environment = Environment(
        loader = FileSystemLoader(['_source', '_includes'])
    )

# Process template pages
print("Generating pages...")
for file in os.listdir('_source/'):
    if file.endswith('.html'):
        page = file[:-5]
        data['page'] = page
        
        print('    {}: {} => {}'.format(page, os.path.join('_source/', file), os.path.join('_output/', file)))
        
        template = environment.get_template(file)
        file = open(os.path.join('_output/', file), 'w')
        file.write(template.render(data=data))
        file.close()
print("Done!")
