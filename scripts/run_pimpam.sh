cd PimPam
make test_all > ../results/pimpam_out.txt
cat ../results/pimpam_out.txt | grep "Data transfer" | awk '{print $4}' > ../results/pimpam_preprocess.txt
cat ../results/pimpam_out.txt | grep "DPU time" | awk '{print $3}' > ../results/pimpam_time.txt
cat ../results/pimpam_out.txt | grep "Lower bound" | awk '{print $3}' > ../results/pimpam_ideal.txt
cd ..
