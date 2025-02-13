#include<iostream>
using namespace std;
class sample 
{
	int a,b;
	public:
	sample()
	{
		a=10;
		b=20;
	}
	void display()
	{
		cout<<"a="<<this<<endl;
		cout<<this->a<<endl;
		cout<<this->b<<endl;
	}
};
main()
{
sample s1;
s1.display();
}
