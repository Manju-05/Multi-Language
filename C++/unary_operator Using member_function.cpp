#include<iostream>
using namespace std;
class sample
{
	int a;
	public:
		sample()
		{
			a=10;
		}
		void display()
		{
			cout<<"a="<<a<<endl;
		}
		void operator++()
		{
			a++;
			++a;
		}
};
main()
{
	sample s1;
	s1.display();//display value 10
	++s1;//calls the operator overloading
	s1.display();
}
