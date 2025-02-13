#include<iostream>
using namespace std;
class sample
{
	int a;
	int b;
	public:
		sample()
		{
			a=10;
			b=20;
		}
		sample(int x)
	{
		a=x;
		b=x;
	}
		sample(int x,int y)
		{
			a=x;
			b=y;
		}
		~sample()
		{
			cout<<"destructor is called"<<endl;
		}
		void display()
		{
			cout<<"a="<<a<<"b="<<b;
		}
	
};

main()
{
	sample s1;
	s1.display();
	sample s2(50);
	s2.display();
	sample s3(100,200);
	s3.display();
	
}

