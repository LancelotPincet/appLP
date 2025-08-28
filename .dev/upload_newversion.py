#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet

"""
Upload new realease for appLP
"""



# %% Libraries
from devlp import path, create_folder
import subprocess
from pathlib import Path



# %% Main function
def main() :
    print('\nRunning upload_newversion :')

    # Warning
    print('     appLP newest version is about to be put online.')
    stop_upload = True
    upload = input("     Are you sure you want to upload appLP new version? y/[n] >>> ")
    if str(upload).lower() in ['yes', 'y', 'true', '1'] :
        upload = input("     This will be definitive are you sure? y/[n] >>> ")
        if str(upload).lower() in ['yes', 'y', 'true', '1'] :
            stop_upload = False
    if stop_upload :
        print('Upload cancelled by user.')
        return None

    # Push subtree
    subprocess.run(["git", "subtree", "push", "--prefix=libsLP/appLP", "appLP", "main"], cwd=path.parent, stdout=subprocess.PIPE, text=True)
    print('     pushed newversion to individual repository')

    # Build project
    create_folder(path.parent / "libsLP/appLP/dist", parent_is_dev=False)
    subprocess.run(["uv", "build", ".", "--out-dir", "dist"], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print('     project built')

    # Get PyPI tokens
    with open(Path.home() / 'LancelotPincet_uv-publish.testpypi_token') as file :
        test_token = file.read()
    print(f'     Got TestPyPI token : {test_token}')
    with open(Path.home() / 'LancelotPincet_uv-publish.pypi_token') as file :
        token = file.read()
    print(f'     Got PyPI token : {token}')

    # Publish TestPyPI
    subprocess.run(["uv", "publish", "--token", test_token, "--publish-url", "https://test.pypi.org/legacy/"], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print("     published to TestPyPI")
    subprocess.run(["uv", "run", "--with", "appLP", "--no-project", "--", "python", "-c", '"import applp"'], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print('     test from TestPyPI import successful')
    
    # Publish PyPI
    subprocess.run(["uv", "publish", "--token", token], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print("     published to PyPI")
    subprocess.run(["uv", "run", "--with", "appLP", "--no-project", "--", "python", "-c", '"import applp"'], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print('     test from PyPI import successful')
    
    # Bump version number
    subprocess.run(["uv", "version", "--bump", "patch"], cwd=path.parent / "libsLP/appLP", stdout=subprocess.PIPE, text=True)
    print("     bumped patch version")

    # End
    print('upload_newversion finished!\n')



# %% Main function run
if __name__ == "__main__":
    main()