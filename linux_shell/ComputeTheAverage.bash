read n

sum=0

for (( i=0; i<n; i++ ));do
    read number
    sum=$((sum + number))
done

average=$(echo "scale = 3: $sum / $n" | bc -l)

printf "%.3f\n" "$average"