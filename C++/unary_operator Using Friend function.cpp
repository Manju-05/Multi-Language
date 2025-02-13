#include<iostream>
using namespace std;
class sample
{
	int a;
	public:
	sample()
	{
		a=10;
	}
	void display()
	{
		cout<<"a="<<a<<endl;
	}
	friend sample operator-(sample t);
};
sample operator-(sample t)
{
	sample temp;
	temp.a=-(t.a);
	return (temp);
}
main()
{
	sample s1,b;
	s1.display();
	 b=-s1;
	 	b.display();
	}
