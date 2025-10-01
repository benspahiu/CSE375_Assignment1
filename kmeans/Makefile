CXX = g++

CXXFLAGS = -O3 -Wall -Werror

SRC_DIR = src
BIN_DIR = bin

SRCS = $(wildcard $(SRC_DIR)/*.cpp)

TARGETS = $(patsubst $(SRC_DIR)/%.cpp, $(BIN_DIR)/%, $(SRCS))

.PHONY: all clean

all: $(TARGETS)

$(BIN_DIR)/%: $(SRC_DIR)/%.cpp
	@mkdir -p $(BIN_DIR) # Create bin directory if it doesn't exist
	$(CXX) $(CXXFLAGS) $< -o $@

$(BIN_DIR)/%: $(SRC_DIR)/%.cpp
	@mkdir -p $(BIN_DIR) # Create bin directory if it doesn't exist
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f $(BIN_DIR)/*
	rmdir $(BIN_DIR) 2>/dev/null || true # Remove directory, ignore errors if empty

# kmeans-serial:
# 	g++ -O3 -Wall -Werror -g -o bin/kmeans-serial kmeans-serial.cpp

# # prime_static:
# # 	g++ -O3 -ltbb -lpthread -Wall -Werror -g -o prime_static prime_static.cpp

# clean_kmeans-serial:
# 	@mkdir -p $(BIN_DIR)
# 	rm -f kmeans-serial

# clean:
# 	rm -f kmeans-serial