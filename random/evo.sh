# read phone.txt file which is given as argument
file_name=$1
while read line; do
    echo $line
done < $file_name

my_function() {
    local name="John"
    echo $name
}

my_function
echo $name