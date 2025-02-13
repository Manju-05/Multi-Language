#include<iostream>
using namespace std;
class addition
{
	public:
	void sum(int a,int b)
	{
		cout<<a+b;
	}
	void sum(int a,int b,int c)
	{
		cout<<a+b+c;
	}
	void sum(double a,double b)
	{
		cout<<a+b;
	}
	void sum(float a,float b)
	{
		cout<<a+b;
	}
};
main()
{
	addition obj;
	obj.sum(10,20);//addition of two parameters
	cout<<endl;
	obj.sum(10,20,30);//addition of three parameters
	cout<<endl;
	obj.sum(10.50,20.50);//double
	cout<<endl;
	obj.sum(10.5000000,2.500000);//float
}
