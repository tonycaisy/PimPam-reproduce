: > results/graphpi_out.txt
for pattern in "3 011101110" "4 0111101111011110" "4 0110100110010110" "5 0110010110110010100100110" "6 011000101110110011010010011101001010"
do
    for graph in $1
    do
        echo "Running GraphPI on $graph with pattern $pattern"
        ./graphpi/build/bin/baseline_test $graph ./graphpi/data/$graph.txt $pattern >> results/graphpi_out.txt
    done
done

cat results/graphpi_out.txt | grep time | awk '{print $2}' > results/graphpi_times.txt
cat results/graphpi_out.txt | grep preprocess | awk '{print $2}' > results/graphpi_preprocess.txt
