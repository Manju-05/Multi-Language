#include<iostream>
using namespace std;
#include<stdlib.h>
#include<conio.h>
#define max_size 100
template<class t>
class queue
{
	
		int i;
		int front;
		int rear;
		int arr_queue[max_size],item;
		public:
	
			queue()
			{
				rear=0;
				front=0;
			}
			void insert()
			{
				if(rear==max_size)
				{
					cout<<"queue is full"<<endl;
				}
				else
				{
				cout<<"enter the item to be inserted"<<endl;
				cin>>item;
				cout<<"inserted value"<<item;
				arr_queue[rear++]=item;	
				}
			}
			void removedata()
			{
				if(front==rear)
				{
					cout<<"\n queue is empty"<<endl;
				}
				else
				{
				cout<<"remove value:"<<arr_queue[front ];
				front++;	
				}
			}
			void display()
			{
				for(i=front;i<rear;i++)
				cout<<"\n position "<<i<<endl<<"value is:"<<item;
				;
			}
};

int main()
{
	int choice ,exit_p=1;
	queue<int>obj;
	do{
		cout<<"\nqueue MainMenu"<<endl;
		cout<<"\n1.insert \n2.removedata \n 3.display \n 4.exit";
		cout<<"enter your choice";
		cin>>choice;
		switch(choice)
		{
			case 1:
				obj.insert();
				break;
				case 2:
				obj.removedata();
				break;
				case 3:
				obj.display();
				break;
				default:exit_p=0;
				break;
		}
	}
		while(exit_p);
	return 0;
	}

