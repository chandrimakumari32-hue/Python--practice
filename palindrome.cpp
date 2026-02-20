// To check whether the number is palindrome or  not
# include<iostream>
using namespace std;
void userinput();
void calculation(int number);
void display(int originalnumber,int reverse);

int main(){
    userinput();
return 0;    
}

void userinput(){
int number;
cout<<"Enter your number"<<endl;
cin>>number;

calculation(number);}

void calculation(int number){
    int reverse=0,rem;
    int originalnumber=number;
    while(number!=0){
    rem=number%10;
    reverse=(reverse*10)+rem;
    number=number/10;
   
    }
  display(originalnumber,reverse);    
}
void display(int originalnumber,int reverse){
if(reverse==originalnumber)
cout<<"Palindrome"<<endl;
else
cout<<"Not palindrome"<<endl;
}
