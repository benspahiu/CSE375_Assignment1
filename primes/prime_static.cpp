#include <iostream>

#include <atomic>
#include <chrono>
#include <tbb/blocked_range.h>
#include <tbb/parallel_for.h>
#include <thread>
#include <vector>

using namespace std;

/// arg_t represents the command-line arguments to the program
struct arg_t {
  int n = 0;
  int num_threads = 1;
  int block_size = 1;

  /// Construct an arg_t from the command-line arguments to the program
  ///
  /// @param argc The number of command-line arguments passed to the program
  /// @param argv The list of command-line arguments
  ///
  /// @throw An integer exception (1) if an invalid argument is given, or if
  ///        `-h` is passed in
  arg_t(int argc, char **argv) {
    long opt;
    while ((opt = getopt(argc, argv, "n:t:b:h")) != -1) {
      switch (opt) {
      case 'n':
        n = atoi(optarg);
        break;
      case 't':
        num_threads = atoi(optarg);
        break;
      case 'b':
        block_size = atoi(optarg);
        break;
      default: // on any error, print a help message.  This case subsumes `-h`
        throw 1;
        return;
      }
    }
    if(n < 1 || num_threads < 1 || block_size < 1){
      throw 1;
      return;
    }
    if(num_threads > 32){
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
         << "  -t [int]    The number of threads [1 - 32]  \n"
         << "  -b [int]    Amount of numbers per task \n"
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
  const int n = args->n;
  const int num_threads = args->num_threads;
  const int block_size = args->block_size;
  const int jump_size = num_threads*block_size;

  auto start = chrono::high_resolution_clock::now();
  atomic<bool> ans;
  
  vector<thread> thread_pool;
  for(int i = 0; i < num_threads; i++){
    thread_pool.push_back(thread([&](int thread){
      // auto thread_start = chrono::high_resolution_clock::now();
      bool local_bool = false;
      for(int start_index = thread*block_size; start_index <= n; start_index += jump_size){
        int end_index = min(start_index + block_size, n + 1);
        for(int j = start_index; j < end_index; j++){
          local_bool = isPrime(j);
        }
      }
      ans = local_bool;
      // auto thread_end = chrono::high_resolution_clock::now();
      // float thread_time = chrono::duration<float>(thread_end - thread_start).count();
      // cout << "Thread " << thread << ": " << thread_time << endl;
    }, i));
  }
  for(thread &t: thread_pool){
    t.join();
  }

  auto end = chrono::high_resolution_clock::now();
  float total_time = chrono::duration<float>(end - start).count();
  (void) ans;

  cout << "Time for [1-" << args-> n << "]: " << total_time << endl;
  delete args;
  return 0;
}