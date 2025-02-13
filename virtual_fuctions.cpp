#include<iostream>
using namespace std;
class a
{
	public:
		virtual void getdata()
		{
			cout<<"baseclass"<<endl;
		}
		void putdata()
		{
			cout<<"welcome to cse"<<endl;
		}
		
};
class b:public a
{
		public:
		void getdata()
		{
			cout<<"derived class"<<endl;
		}
		void putdata()
		{
			cout<<"welcome to cse";
		}
};
int main()
{
	a obj1;
	b obj2;
	a*ptr;
	ptr=&obj1;
	ptr->getdata();
	ptr->putdata();
	ptr=&obj2;
	ptr->getdata();
	ptr->putdata();
}
