: > results/pangolin_out.txt
for graph in $1
do
    for clique in 3 4 5
    do
        echo "Running Pangolin on $graph with clique $clique"
        ./pangolin/bin/pangolin/kcl_base ./pangolin/data/$graph/graph $clique >> results/pangolin_out.txt
    done
done

cat results/pangolin_out.txt | grep "runtime" | awk '{print $4}' > results/pangolin_time.txt
