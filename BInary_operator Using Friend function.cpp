#include<iostream>
using namespace std;
class test2;
class test1
{
	int x;
	public:
	void getx()
	{
	
		cout<<"enter the value of x"<<endl;
			cin>>x;
	}
	friend void operator>(test1,test2);
};
class test2
{
	int y;
	public:
	void gety()
	{

	cout<<"enter the value of y"<<endl;
			cin>>y;
	}
	friend void operator>(test1,test2);
};
void operator>(test1 t1,test2 t2)
{
	if(t1.x>t2.y)
	{
		cout<<"x is greater="<<t1.x<<endl;
	}
	else
	{
		cout<<"y is greater="<<t2.y<<endl;
	}
}
main()
{
	test1 a;
	test2 b;
	a.getx();
	b.gety();
    a>b;//calls the operator overloading...
	return 0;
}
