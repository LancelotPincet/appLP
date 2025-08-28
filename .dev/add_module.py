#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Create new module for appLP
"""



# %% Libraries
from devlp import path
from datetime import datetime
import os
import json



# %% Main function
def main() :
    print('\nRunning add_module :')

    # Ask for script name
    already_exists = True
    while already_exists :
        name = input('     New module name ? >>> ')
        module_path = path.parent / f'libsLP/appLP/src/applp/modules/{name}_LP'
        script_path = path.parent / f'libsLP/appLP/src/applp/scripts/{name}_LP'
        if module_path.exists() :
            print('     This module already exists :/')
            crush = input("     Do you want to crush existing module? y/[no] >>> ")
            if str(crush).lower() in ["y", "yes", "true", "1"] :
                crush = input("     Sure? y/[no] >>> ")
                if str(crush).lower() in ["y", "yes", "true", "1"] :
                    already_exists = False
        elif script_path.exists() :
            print('     This module already exists as a script :/')
        else :
            already_exists = False
    description = input('     what will the module do ? >>> ')
    date = datetime.now().strftime("%Y-%m-%d")

    # Print informations
    print(f'     name : {name}')
    print(f'     description : {description}')
    print(f'     date : {date}')
    if not module_path.exists() :
        os.mkdir(module_path)

    # Function to copy file
    def copy_file(from_path, to_path) :
        string = from_path.read_text()
        string = string.replace('template_modulename', name)
        string = string.replace('template_moduledate', date)
        string = string.replace('template_moduledescription', description)
        string = string.replace('template_modulelib', "appLP")
        string = string.replace('template_modulelowerlib', "applp")
        string = string.replace('template_moduleequals', "="*len(name))
        string = string.replace('template_modlibeq', "="*len("appLP"))
        to_path.write_text(string)
        
    # Write python module
    python_path = path / '_templates/lib_module.txt'
    newpython_path = module_path / f'{name}.py'
    copy_file(python_path, newpython_path)
    with open(module_path / "__init__.py", "w") as file :
        file.write("")
    print('     Module file written [to complete]')

    # Add test
    python_path = path / '_templates/lib_test.txt'
    newpython_path = module_path / f'test_{name}.py'
    copy_file(python_path, newpython_path)
    print('     Test file written [to complete]')

    # Add module to json file
    modjson = {}
    modjson['module'] = f"modules/{name}_LP/{name}"
    modjson['object'] = name
    modjson['description'] = description
    modjson['date'] = date
    json_path = path.parent / f'libsLP/appLP/src/applp/modules.json'
    with open(json_path, "r") as file :
        data = json.load(file)
    data[name] = modjson
    with open(json_path, "w") as file :
        json.dump(data, file, indent=4, sort_keys=True)
    print("     Module json updated")

    # Create documentation
    if name[0] == (name.lower())[0] : # if function
        rst_path = path / '_templates/lib_docaddfunction.rst'
    else : # Class
        rst_path = path / '_templates/lib_docaddclass.rst'
    newrst_path = path.parent / f'libsLP/appLP/docs/source/{name}.rst'
    copy_file(rst_path, newrst_path)

    allmodules_path = path.parent / f'libsLP/appLP/docs/source/modules.rst'
    string = allmodules_path.read_text()
    string = string.replace(f"   {name}\n", "")
    with open(allmodules_path, "w") as file :
        file.write(string)
    with open(allmodules_path, "a") as file :
        file.write(f"   {name}\n")

    print('     Documentation rst file added')

    # End
    print('add_module finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()