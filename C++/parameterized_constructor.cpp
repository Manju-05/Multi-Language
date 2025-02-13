#include<iostream>
using namespace std;
class sample 
{
		int a;
		int b;
		public:
		sample(int x,int y)
		{
			a=x;
			b=y;
		}
		void display()
		{
			cout<<"a="<<a<<endl;
			cout<<"b="<<b<<endl;
		}
};
main()
{
	sample s1(47,99);   
	s1.display();
}
