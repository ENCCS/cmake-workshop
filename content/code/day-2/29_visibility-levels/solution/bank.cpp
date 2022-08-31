#include <cstdlib>
#include <iostream>

#include "account.hpp"

int main() {
  auto acc = Account();

  std::cout << "Depositing 100.0" << std::endl;
  acc.deposit(100.0);
  std::cout << "  Balance: " << acc.get_balance() << std::endl;

  std::cout << "Withdrawing 50.0" << std::endl;
  acc.withdraw(50.0);
  std::cout << "  Balance: " << acc.get_balance() << std::endl;

  std::cout << "Withdrawing 60.0" << std::endl;
  acc.withdraw(60.0);
  std::cout << "  Balance: " << acc.get_balance() << std::endl;

  return EXIT_SUCCESS;
}
