#include<iostream>
using namespace std;
main()
{
	int *ptr1=new int(10);
	int *ptr2=new int(20);
	int total;
	total=*ptr1+*ptr2;	
	cout<<"total="<<total;
	delete ptr1;
}
