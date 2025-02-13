#include<iostream>
using namespace std;
template<class T>
void swap(T&a,T&b)
{
	T temp;
	temp=a;
	a=b;
	b=temp;
}
main()
{
	int x=10;
	int y=20;
	cout<<"x="<<x<<"\t y="<<y<<endl;
	swap(x,y);
      cout<<"x="<<x<<"\t y="<<y<<endl;
return 0;
}
