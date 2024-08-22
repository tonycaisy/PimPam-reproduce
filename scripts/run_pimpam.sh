cd PimPam

# run pimpam
echo "Running PimPam"
make test_all > ../results/pimpam_out.txt
cat ../results/pimpam_out.txt | grep "Data transfer" | awk '{print $5}' > ../results/pimpam_preprocess.txt
cat ../results/pimpam_out.txt | grep "DPU time" | awk '{print $4}' > ../results/pimpam_time.txt
cat ../results/pimpam_out.txt | grep "Lower bound" | awk '{print $3}' > ../results/pimpam_ideal.txt

# run pimpam without thread level collaboration
echo "Running PimPam without thread level collaboration"
OVERRIDE=-DBRANCH_LEVEL_THRESHOLD=2147483647 make test_all | grep "DPU time" | awk '{print $4}' > ../results/pimpam_no_col.txt

# run pimpam without load aware assignment
echo "Running PimPam without load aware assignment"
OVERRIDE=-DNO_LOAD_BALANCE make test_all | grep "DPU time" | awk '{print $4}' > ../results/pimpam_no_balance.txt

# run pimpam without bitmap
echo "Running PimPam without bitmap"
make test_bitmap | grep "DPU time" | awk '{print $4}' > ../results/pimpam_bitmap.txt
OVERRIDE=-DNO_BITMAP make test_bitmap | grep "DPU time" | awk '{print $4}' > ../results/pimpam_no_bitmap.txt

# test predict model accuracy
echo "Testing model accuracy"
GRAPH=LJ PATTERN=CLIQUE4 make test > /dev/null
cp result/clique4_soc-LiveJournal1.txt ../results/accuracy_C4.txt
GRAPH=LJ PATTERN=CYCLE4 make test > /dev/null
cp result/cycle4_soc-LiveJournal1.txt ../results/accuracy_R4.txt
GRAPH=LJ PATTERN=TRI_TRI6 make test > /dev/null
cp result/tri_tri6_soc-LiveJournal1.txt ../results/accuracy_T6.txt

# test model tradeoff
echo "Testing model tradeoff"
: > ../results/pimpam_out.txt
for graph in YT PT LJ
do
    for pattern in CLIQUE3 CYCLE4 TRI_TRI6
    do
        OVERRIDE=-DMORE_ACCURATE_MODEL GRAPH=$graph PATTERN=$pattern make test >> ../results/pimpam_out.txt
    done
done
cat ../results/pimpam_out.txt | grep "Data transfer" | awk '{print $5}' > ../results/pimpam_model_preprocess.txt
cat ../results/pimpam_out.txt | grep "DPU time" | awk '{print $4}' > ../results/pimpam_model_time.txt

# test threshold
echo "Testing threshold"
: > ../results/pimpam_out.txt
for threshold in 1 2 4 8 16 32 64
do
    for graph in PP YT PT
    do
        for pattern in CLIQUE3 TRI_TRI6
        do
            OVERRIDE=-DBRANCH_LEVEL_THRESHOLD=$threshold GRAPH=$graph PATTERN=$pattern make test >> ../results/pimpam_out.txt
        done
    done
done
cat ../results/pimpam_out.txt | grep "DPU time" | awk '{print $4}' > ../results/pimpam_threshold_time.txt

cd ..
