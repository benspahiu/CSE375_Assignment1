CXX = g++

CXXFLAGS = -O3 -Wall -Werror
LDFLAGS  = -ltbb #-lpthread

SRC_DIR = src
BIN_DIR = bin

SRCS = $(wildcard $(SRC_DIR)/*.cpp)
NAMES = $(basename $(notdir $(SRCS)))
TARGETS = $(addprefix $(BIN_DIR)/, $(NAMES))

.PHONY: all clean clean-% $(NAMES)

all: $(TARGETS)

$(BIN_DIR)/%: $(SRC_DIR)/%.cpp
	@mkdir -p $(BIN_DIR) # Create bin directory if it doesn't exist
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $< -o $@

$(NAMES): %: $(BIN_DIR)/%

clean:
	rm -f $(BIN_DIR)/*
	rmdir $(BIN_DIR) 2>/dev/null || true # Remove directory, ignore errors if empty

clean-%:
	rm -f $(BIN_DIR)/$*

clean-results:
	rm -f results/*