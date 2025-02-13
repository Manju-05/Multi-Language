#include<iostream>
using namespace std;
class bc
{
	public:
		int x,y;
		void getxy()
		{
			x=10;
			y=20;
			cout<<"x="<<x<<endl;
			cout<<"y="<<y<<endl;
		}
};
class dc1:public bc
{
	public:
		int a;
		void add()
		{
			a=x+y;
			cout<<"addition:"<<a<<endl;
		}
};

class dc2:public bc
{
	public:
		int b;
		void sub()
		{
			b=x-y;
			cout<<"subtraction:"<<b<<endl;
		}
};


class dc3:public bc
{
	public:
		int m;
		void mult()
		{
			m=x*y;
			cout<<"multiplication:"<<m<<endl;
		}
};

main()
{
	dc1 obj1;
	dc2 obj2;
	dc3 obj3;
	obj1.getxy();
	obj1.add();
	obj2.getxy();
	obj2.sub();
	obj3.getxy();
	obj3.mult();
}




