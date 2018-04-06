#include <iostream>
using namespace std;
long double factorial(int);
int main(){
	cout << factorial(5) << endl;
}

long double factorial(int n)
{
	long double fact;
	if(n==0)
		return 1;
	else
		return n*factorial(n-1);
}


