graph := wiki-Vote p2p-Gnutella04 ca-AstroPh com-youtube cit-Patents soc-LiveJournal1

.PHONY: all

all: ./reproduce/fig11.pdf ./reproduce/tab3.csv ./reproduce/fig12.pdf ./reproduce/fig13-3.png ./reproduce/fig14.pdf ./reproduce/tab4.py ./reproduce/fig15.pdf ./reproduce/fig16.pdf ./reproduce/fig17.pdf

./reproduce/fig11.pdf: ./scripts/fig11.py ./results/pimpam_time.txt ./results/graphpi_time.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig11.pdf

./reproduce/tab3.csv: ./scripts/tab3.py ./results/pimpam_preprocess.txt ./results/graphpi_preprocess.txt
	@mkdir -p reproduce
	@python3 $<

./reproduce/fig12.pdf: ./scripts/fig12.py ./results/pimpam_time.txt ./results/pimpam_no_col.txt ./results/pimpam_no_balance.txt ./results/pimpam_ideal.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig12.pdf

./reproduce/fig13-3.png: ./scripts/fig13.py ./results/accuracy_C4.txt ./results/accuracy_R4.txt ./results/accuracy_T6.txt
	@mkdir -p reproduce
	@python3 $<

./reproduce/fig14.pdf: ./scripts/fig14.py ./results/pimpam_bitmap.txt ./results/pimpam_no_bitmap.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig14.pdf

./reproduce/tab4.py: ./scripts/tab4.py ./results/pimpam_time.txt ./results/pimpam_preprocess.txt ./results/pimpam_model_time.txt ./results/pimpam_model_preprocess.txt
	@mkdir -p reproduce
	@python3 $<

./reproduce/fig15.pdf: ./scripts/fig15.py ./results/pimpam_threshold_time.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig15.pdf

./reproduce/fig16.pdf: ./scripts/fig16.py ./results/pangolin_time.txt ./results/pimpam_time.txt ./results/pimpam_bitmap.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig16.pdf

./reproduce/fig17.pdf: ./scripts/fig17.py ./results/pimpam_time.txt ./scripts/khuzdul_time.txt
	@mkdir -p reproduce
	@python3 $<
	@rm -rf fig17.pdf

.PHONY: run_pimpam run_graphpi run_pangolin

run_pimpam: data_pimpam ./scripts/run_pimpam.sh
	@mkdir -p results
	@bash ./scripts/run_pimpam.sh

run_graphpi: data_graphpi ./scripts/run_graphpi.sh ./graphpi/build/bin/baseline_test
	@mkdir -p results
	@bash ./scripts/run_graphpi.sh "$(graph)"

./graphpi/build/bin/baseline_test:
	@cd graphpi && mkdir -p build && cd build && cmake .. && make -j

run_pangolin: data_pangolin ./scripts/run_pangolin.sh ./pangolin/bin/pangolin/kcl_base
	@mkdir -p results
	@bash ./scripts/run_pangolin.sh "$(graph)"

./pangolin/bin/pangolin/kcl_base:
	mkdir -p pangolin/bin/pangolin
	@cd pangolin/src/pangolin/clique && make

# prepare data
./data/%.txt:
	@mkdir -p data
	@wget http://snap.stanford.edu/data/$*.txt.gz -O ./data/$*.txt.gz
	@gzip -d ./data/$*.txt.gz

./data/com-youtube.txt:   # special for youtube
	@mkdir -p data
	@wget http://snap.stanford.edu/data/bigdata/communities/com-youtube.ungraph.txt.gz -O ./data/com-youtube.txt.gz
	@gzip -d ./data/com-youtube.txt.gz

./data-cleaned/%.txt: ./data/%.txt ./bin/raw_data_clean
	@mkdir -p data-cleaned
	@./bin/raw_data_clean < $< > $@

./bin/raw_data_clean: ./scripts/raw_data_clean.cpp
	@mkdir -p bin
	@g++ -o $@ $<


.PHONY: data_pimpam data_graphpi data_pangolin
.SECONDARY:

# prepare data for PimPam
data_pimpam: $(foreach g, $(graph), ./PimPam/data/$(g).bin)

./PimPam/data/%.bin: ./data-cleaned/%.txt ./bin/to_pimpam
	@mkdir -p PimPam/data
	@./bin/to_pimpam < $< > $@

./bin/to_pimpam: ./scripts/to_pimpam.cpp
	@mkdir -p bin
	@g++ -o $@ $<

# prepare data for GraphPi
data_graphpi: $(foreach g, $(graph), ./graphpi/data/$(g).txt)

./graphpi/data/%.txt: ./data-cleaned/%.txt ./bin/to_graphpi
	@mkdir -p graphpi/data
	@./bin/to_graphpi < $< > $@

./bin/to_graphpi: ./scripts/to_graphpi.cpp
	@mkdir -p bin
	@g++ -o $@ $<

# prepare data for Pangolin
data_pangolin: $(foreach g, $(graph), ./pangolin/data/$(g))

./pangolin/data/%: ./data-cleaned/%.txt ./bin/to_pangolin
	@mkdir -p $@
	@cd $@ && ../../../bin/to_pangolin < ../../../$<

./bin/to_pangolin: ./scripts/to_pangolin.cpp
	@mkdir -p bin
	@g++ -o $@ $<
