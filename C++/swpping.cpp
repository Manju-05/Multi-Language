#include <iostream>
using namespace std;
template <class t>
void swap(t&a,t&b);
{
  t temp;
  temp=a;
  a=b;
  b=temp;
  }
  int main()
  {
  	int x=10,y=20;
    cout << "Before swapping." << endl
    cout << "a = " << a << ", b = " << b << endl;


    cout << "\nAfter swapping." << endl;
    swap(x,y)
    cout << "a = " << a << ", b = " << b << endl;

    return 0;
  }

