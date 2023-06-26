#!/bin/bash

# This script creates a project template for a new project.
# It creates a directory with the project name, and creates a README.md file in it.

# Check if the user has provided a project name
if [ $# -eq 0 ]
then
    echo "Please provide a project name."
    exit 1
fi

# Create a directory with the project name
mkdir $1

# Create a README.md file in the directory
touch $1/README.md

# create folders
mkdir $1/data
mkdir $1/data/0_raw
mkdir $1/references
mkdir $1/results
mkdir $1/notebooks
mkdir $1/reports
mkdir $1/tests
mkdir $1/docs
mkdir $1/src
mkdir $1/tmp

# Create a .gitignore file in the directory
touch $1/.gitignore

# Add the following lines to the .gitignore file
echo "data/" >> $1/.gitignore
echo "references/" >> $1/.gitignore
echo "tmp/" >> $1/.gitignore



