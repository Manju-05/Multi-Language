#include<iostream>
using namespace std;
class bc
{
	public:
		int x;
		void getx()
		{
			x=100;
			cout<<"x="<<x<<endl;
		}
};
class dc1:public bc
{
	public:
		int y;
		void gety()
		{
			y=200;
			cout<<"y="<<y<<endl;
		}
};
class dc2:public dc1
{
	public:
	int z;
	void add()
	{
		z=x+y;
		cout<<"z="<<z<<endl;
		}	
};
 int main()
{
	dc2 obj;
	obj.getx();
	obj.gety();
	obj.add();
	return 0;
}

