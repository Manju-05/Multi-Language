#include<iostream>
using namespace std;
class baseclass
{
	public:
	int a,b;
	void getdata()
	{
		a=10;
		b=20;
	cout<<"a="<<a<<endl;
	cout<<"b="<<b<<endl;
	}	
};
class derived:public baseclass
{
	public:
		int z;
		void add()
		{
			z=a+b;
			cout<<"z="<<z;
		}
};
main()
{
	derived obj;
	obj.getdata();
	obj.add();
	return 0;	
}








