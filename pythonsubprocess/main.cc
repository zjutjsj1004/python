#include <iostream>
#include <fstream>
/*
int main(){
  const char* input[] = {"1", "2", "3", "4", "5"};
  int ret = do_check(5, input);
  ret = 555;
  std::ofstream outfile;
  outfile.open("afile.txt");
  outfile << ret;
  outfile.close();
  if (0 == ret)
  {
      std::cout << ret;
  }
  else {
      std::cerr << ret;
  }
  exit(666);
  return ret;
}*/

int main() {

  // https://stackoverflow.com/questions/3734102/why-cant-i-return-bigger-values-from-main-function
  //return 256; // 因为返回值main在UNIX 上被限制在[0, 255] 范围内， 我们返回256，会使得变成0。 不过可以通过stdout和stderr输出
  int ret = 200;
  std::cerr << 5000;
  return ret;
}