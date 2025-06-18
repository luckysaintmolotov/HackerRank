#!/bin/bash
read stdin

yes=("Y" "y")
no=("N" "n")

if [[ " ${yes[@]} " =~ " $stdin " ]]; then
  echo "YES"
else
  echo "NO"
fi
