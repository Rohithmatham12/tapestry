# This file is included in the top-level Makefile

FLOWER_WAN_SPIKE_DIR := contrib/jneums-flower-wan-spike

.PHONY: flower-wan-spike-all flower-wan-spike-tests

flower-wan-spike-all:: flower-wan-spike-tests

flower-wan-spike-tests::
	@echo "${INFO}Running the Flower WAN spike unit tests...${_END}"
	cd ${FLOWER_WAN_SPIKE_DIR}; uv run python -m unittest discover -s tests
