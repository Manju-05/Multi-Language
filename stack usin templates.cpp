#include<iostream>
#include<string>
using namespace std;
#define size 5
template <class T> 
class stack
{
	int top;
	T st[size];
	public:
	stack()
	{
		top=-1;
	}
	void push(T k)
	{
		if(isfull())
		{
			cout<<"stack is full";
		}
		else
		{
			cout<<"inserted element"<<k<<endl;
				st[top]=k;
			top++;
		
		}
	}
	T pop()
	{
		T poppedelement=st[top];
		top--;
	}
	 T topelement()
	 {
	T topelement=st[top];
	return topelement;
	 }
	 bool isfull()
	 {
	 	if(top==size-1)
		return 1;
		else 
		return 0; 
	 }
	 bool isempty()
	 {
	 	if(top=-1)
		return 1;
		else 
		return 0;
	 }	
};
int main()
	{
		stack<int>istack;
		istack.push(10);
		istack.push(20);
		istack.push(30);
		cout<<istack.pop()<<"is removed from stack"<<endl;
		cout<<"top element is:"<<istack.topelement()<<endl;
			return 0;
	}

