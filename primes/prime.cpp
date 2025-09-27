#include <iostream>

#include <atomic>
#include <chrono>
#include <tbb/blocked_range.h>
#include <tbb/parallel_for.h>

using namespace std;

/// arg_t represents the command-line arguments to the program
struct arg_t {
  int n = 0;

  /// Construct an arg_t from the command-line arguments to the program
  ///
  /// @param argc The number of command-line arguments passed to the program
  /// @param argv The list of command-line arguments
  ///
  /// @throw An integer exception (1) if an invalid argument is given, or if
  ///        `-h` is passed in
  arg_t(int argc, char **argv) {
    long opt;
    while ((opt = getopt(argc, argv, "n:h")) != -1) {
      switch (opt) {
      case 'n':
        n = atoi(optarg);
        break;
      default: // on any error, print a help message.  This case subsumes `-h`
        throw 1;
        return;
      }
    }
    if(n < 1){
      throw 1;
      return;
    }
  }

  /// Display a help message to explain how the command-line parameters for this
  /// program work
  ///
  /// @progname The name of the program
  static void usage(char *progname) {
    cout << basename(progname) << ": program that iterates from 1 to n, checking which numbers are prime\n"
         << "  -n [int]    The last integer to check (1 to n)  \n"
         << "  -h          Print help (this message)\n";
  }
};

bool isPrime(int n){
  if(n <= 1){
    return false;
  }
  for(int i = 2; i < n; i++){
    if(n % i == 0){
      return false;
    }
  }
  return true;
}

int main(int argc, char **argv){
  arg_t *args;
  try {
    args = new arg_t(argc, argv);
  } catch (int i) {
    arg_t::usage(argv[0]);
    return 1;
  }

  auto start = chrono::high_resolution_clock::now();
  atomic<bool> ans;
  
  tbb::parallel_for(
    tbb::blocked_range<int>(1, args->n),
    [&](const tbb::blocked_range<int>& range){
      bool local_bool = false;
      for(int i = range.begin(); i < range.end(); i++){
        local_bool = isPrime(i);
      }
      ans = local_bool;
    }
  );

  auto end = chrono::high_resolution_clock::now();
  float total_time = chrono::duration<float>(end - start).count();
  (void) ans;

  cout << "Time for [1-" << args-> n << "]: " << total_time << endl;
  return 0;
}