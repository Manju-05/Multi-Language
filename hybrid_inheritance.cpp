#include<iostream>
using namespace std;
class a
{
	public:
	int x;
	void getx()
	{
		x=10;
		cout<<"x="<<x<<endl;
	}
};

class b:public a
{
	public:
		int y;
		void gety()
		{
			y=20;
			cout<<"y="<<y<<endl;
		}
	
};
class c
{
	public:
		int z;
		void getz()
		{
			z=30;
			cout<<"z="<<z<<endl;
		}
};

class d:public b,public c
{
	public:
	int s;
	void add()
	{
		s=x+y+z;
		cout<<"Addition of three numbers:"<<s<<endl;
	}
};
main()
{
	d obj;
	obj.getx();
	obj.gety();
	obj.getz();
	obj.add();
}

