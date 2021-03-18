#include <torch/torch.h> // One-stop header.
#include <iostream>

int main() {
  torch::Tensor tensor = torch::eye(3);
  std::cout << tensor << std::endl;
}