#include<iostream>
using namespace std;
struct bnode
{
  int bit;
  
  bnode *next;
  bnode *prev;
};
bnode *temp,*temp1,*temp2;
class DLL
{
    
	
	public:
	int n;
	bnode *head,*tail;
 	DLL()
 	{
 	  head=tail=NULL;
 	}
 	void create();
 	void display();
 	void comp1();
 	void comp2();
 	void addition(DLL d1);
 	
 };
 void DLL::create()
 {
 	cout<<"\nEnter Decimal number ";
 	cin>>n;
 	while(n>0)
 	{
 		bnode *nnode=new bnode;
 		nnode->prev=nnode->next=NULL;
 		nnode->bit=n%2;
 		n=int(n/2);
 		if(head==NULL)
 		{
			head=tail=nnode;
		}
		else
		{
			nnode->next=head;
			head->prev=nnode;
			head=nnode;
		}
	}
	
}

void DLL::display()
  {
    cout<<"Binary representation = \n";
    temp=head;
    
    while(temp!=NULL)
    {
      cout<<temp->bit;
      temp=temp->next;
      
    }
    cout<<endl;
  } 	

void DLL::comp1()
{
	cout<<"\n1's complement =  ";
	temp=head;
	while(temp!=NULL)
	{
		if(temp->bit==1)
		{
			cout<<0;
		}
		else
		{
			cout<<1;
		}
		temp=temp->next;
	}
	cout<<endl;
}

void DLL::comp2()
{

  temp=tail;

	while(temp->bit!=1)
	{
		temp=temp->prev;
	}
	temp=temp->prev;
	while(temp!=NULL)
	{
		if(temp->bit==1)
		{
			temp->bit=0;
		}
		else
		{
			temp->bit=1;
		}
		temp=temp->prev;
	}
	cout<<"2's compliment ";
	
	display();	
}
void DLL::addition(DLL d1)
{
	int carry=0;
 	
	temp1=tail;
	temp2=d1.tail;
	head=tail=NULL;
	while(temp1!=NULL && temp2!=NULL )
	{
		bnode *nnode=new bnode;
 		nnode->prev=nnode->next=NULL;
 		
 		
		if(temp1->bit==0 && temp2->bit==0 && carry==0)
		{
			nnode->bit=0;
			carry=0;
		}
		else if(temp1->bit==0 && temp2->bit==0 && carry==1)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp1->bit==0 && temp2->bit==1 && carry==0)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp1->bit==0 && temp2->bit==1 && carry==1)
		{
			nnode->bit=0;
			carry=1;
		}
		else if(temp1->bit==1 && temp2->bit==0 && carry==0)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp1->bit==1 && temp2->bit==0 && carry==1)
		{
			nnode->bit=0;
			carry=1;
		}
		else if(temp1->bit==1 && temp2->bit==1 && carry==0)
		{
			nnode->bit=0;
			carry=1;
		}
		else if(temp1->bit==1 && temp2->bit==1 && carry==1)
		{
			nnode->bit=1;
			carry=1;
		}
		if(head==NULL)
 		{
			head=tail=nnode;
		}
		else
		{
			nnode->next=head;
			head->prev=nnode;
			head=nnode;
		}
		temp1=temp1->prev;
		temp2=temp2->prev;
	}
	while(temp1!=NULL)
	{
		bnode *nnode=new bnode;
		nnode->prev=nnode->next=NULL;
	
		if(temp1->bit==0 && carry==0)
		{
			nnode->bit=0;
			carry=0;
		}
		else if(temp1->bit==0 && carry==1)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp1->bit==1 && carry==0)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp1->bit==1 && carry==1)
		{
			nnode->bit=0;
			carry=1;
		}
			nnode->next=head;
			head->prev=nnode;
			head=nnode;
		temp1=temp1->prev;
	}
	while(temp2!=NULL)
	{
		bnode *nnode=new bnode;
		nnode->prev=nnode->next=NULL;
		
		if(temp2->bit==0 && carry==0)
		{
			nnode->bit=0;
			carry=0;
		}
		else if(temp2->bit==0 && carry==1)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp2->bit==1 && carry==0)
		{
			nnode->bit=1;
			carry=0;
		}
		else if(temp2->bit==1 && carry==1)
		{
			nnode->bit=0;
			carry=1;
		}
			nnode->next=head;
			head->prev=nnode;
			head=nnode;        
		temp2=temp2->prev;
	}
	if(carry==1)
	{
		
		bnode *nnode=new bnode;
 		nnode->prev=nnode->next=NULL;
		nnode->bit=1;
		nnode->next=head;
		head->prev=nnode;
		head=nnode;
	}
	cout<<"Addition's ";
	display();	
		
}
int main()
{
 	DLL d1,d2,d3;
 	d1.create();
 	d1.display();
 	d1.comp1();
 	d1.comp2();
 	d2.create();
 	d3.create();
 	d2.addition(d3);
        return(0);
 }	
	
	
	
	
	 		
