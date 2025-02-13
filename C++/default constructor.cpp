#include<iostream>
using namespace std;
class sample
{
	int a;
	int b;
	public:
		sample()
		{
			a=47;
			b=99;
		}
		void display()
		{
			cout<<"a="<<a<<endl;
			cout<<"b="<<b<<endl;
		}
};
main()
{
	sample s1;
s1.display();
}

