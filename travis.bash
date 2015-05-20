#!/bin/bash

check_file () {
    if [ -f "$1" ]
    then
        echo "$1 found"
    else
        echo "$1 not found"
        exit -1
    fi
}

echo "Check for files (Including the core file for the program)"

check_file "apiary.apib"
check_file "IDB.log"
check_file "models.html"
check_file "models.py"
check_file "tests.py"
check_file "tests.out"
check_file "UML.pdf"
check_file "README.md"
check_file "programmerJobs.py"