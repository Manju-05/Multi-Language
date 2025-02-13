#include<iostream>
using namespace std;
class bc1
{
	public:
		int x;
		void getx()
		{
			x=10;
			cout<<"x="<<x<<endl;
		}
	
};
class bc2
{
	public:
		int y;
		void gety()
		{
			y=20;
			cout<<"y="<<y<<endl;
		}
};
class dc1:public bc1, public bc2
{
	public:
		int z;
		void add()
		{
			z=x+y;
			cout<<"z="<<z<<endl;
		}
};
main()
{
	dc1 obj;
	obj.getx();
	obj.gety();
	obj.add();
	return 0;
}
