#include<iostream>
using namespace std;
class sample
{
	int a;
	public:
		sample()
		{
			a=0;
		}
	sample(int x)
	{
		a=x;
	}
	void display()
	{
		cout<<"a="<<a<<endl;
	}
	sample operator + (sample &t)
	{
		sample temp;
		temp.a=a+t.a;
		return(temp);
	}
};
int main()
{
	sample s1(10);
	sample s2(20);
	sample s3;
	s1.display();
	s2.display();
	s3=s1+s2;
	s3.display();
}
