#include <cstdlib>
#include <iostream>

#include "config.h"

int main() {
  std::cout << "Number of physical cores: " << NUMBER_OF_PHYSICAL_CORES
            << std::endl;

  std::cout << "Total physical memory in megabytes: " << TOTAL_PHYSICAL_MEMORY
            << std::endl;

  std::cout << "OS name: " << OS_NAME << std::endl;
  std::cout << "OS platform: " << OS_PLATFORM << std::endl;

  return EXIT_SUCCESS;
}
