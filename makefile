graph := wiki-Vote p2p-Gnutella04 ca-AstroPh com-youtube cit-Patents soc-LiveJournal1

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
