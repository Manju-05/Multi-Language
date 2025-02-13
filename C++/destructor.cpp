#include<iostream>
using namespace std;
class sample
{
	int a,b,x;
	public:
		sample()  //constructor
		{
		a=10;
		b=20;
		
		}
	void add()   //memberfunction for addition of two numbers....
	{
		x=a+b;
		cout<<"addition of two numbers:"<<x<<endl;
	}
	~sample()  //deconstructor...
	{
		cout<<"destructor is called";
    }
};
 int main()
{
	sample obj;
	obj.add();
	
}
