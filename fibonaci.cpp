#include <iostream>
using namespace std;
long double fibonaci(int);
int main(){
	cout << fibonaci(999) <<endl;
}

long double fibonaci(int n)
{
	long double fib;
	if (n==0)
		return 0;
	if (n==1)
		return 1;
	else
		return fibonaci(n-1) + fibonaci(n-2);
}


