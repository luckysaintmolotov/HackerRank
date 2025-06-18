#!/bin/bash
read x
read y

sum=$((x + y))
echo "$sum"
difference=$((x - y))
echo "$difference"
product=$((x * y))
echo "$product"
if [ "$y" -ne 0 ]; then
    quotient=$((x / y))
    echo "$quotient"
else
    echo "Cannot divide by zero."
fi
