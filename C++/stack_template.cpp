#include<iostream>
#include<string>
using namespace std;
#define max_size
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
		void push( T,K)
		{
			if(isfull())
			{
				cout<<"stack is full"<<endl;
			}
			else
			{
				cout<<"insert element"<<K<<endl;
				top++;
				st[top=k];		
			}
		}
		T pop()
		{
			T popped element=st[top];
				top--;
		}
		T top element
{			
		T top element =st[top];
		return top element;
}
		bool is full()
		{
			
			if(top==size-1)
			return 1;
		}
		else
		{
			return 0;
		}
		bool is empty()
		{
			if(top==-1)
			return 1;
			else
			return 0;
		}	
	};
	
	main()
	{
		stack<int>istack
		istack.push[2];
		istack.push[54];
		istack.push[255];
		cou<<istack.pop()<<"is removed from stack"<<endl;
		cout<<"top element is:"<<istack.top element(1)<<endl;
	return 0;
	}
	

	
