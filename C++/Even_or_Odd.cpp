#include <string>

using namespace std;

string even_or_odd(int number) 
{
  
  if(number%2 == 0){
    return "Even"; 
    }
  else if(number %2 != 0){
    return "Odd";
  }
  return "";
}