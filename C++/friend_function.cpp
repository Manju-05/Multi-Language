 #include<iostream>
 using namespace std;
 class sample 
 {
 int a,b;
 public:
 	void getdata()
 	{
 		cout<<"enter the value of a:";
 		cin>>a;
 		cout<<"enter the value of b:";
 		cin>>b;
}
friend void putdata(sample);
	  };

	  void putdata(sample s1)
	 {
	 	cout<<s1.a;
	 	cout<<s1.b;
	 }
	 main()
	 {
	 	sample s1;
	 	s1.getdata();
	 	putdata(s1);
	 }

