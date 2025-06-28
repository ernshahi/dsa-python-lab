#!/bin/bash

# Variables
## Concatenation
greeting="Hello"
name="World"
echo "$greeting $name"

## Arithmetic
num1=5
num2=10
echo "$num1 $num2"
sum=$((num1 + num2))
echo "The sum is $sum"

## Data Types
# Array example
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
  echo $fruit
done

languages=("Python" "Java" "C++" "JavaScript")
for language in "${languages[@]}"; do
    echo $language
done