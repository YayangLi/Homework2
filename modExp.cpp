#include <iostream>
#include <cstdio>
using namespace std;

int recModExp(int x,int y,int P)
{
     if(y == 0)
        return 1;

     int z = recModExp(x, y / 2, P);
     if(y % 2 == 0)
        return z * z % P;
     else
        return x * z * z % P;
}

int main()
{
   int x , y, P;
   int ans;
   cout<<"input the base number:";
   cin>>x;

   cout<<"input the exponent:";
   cin>>y;

   cout<<"input the module:";
   cin>>P;

   ans = recModExp(x, y, P);
   cout<<ans<<endl;
    return 0;
}


