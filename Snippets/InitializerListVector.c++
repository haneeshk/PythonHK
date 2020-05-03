#include<iostream>
#include<vector>

int i=24;
double v[]={1.0,2.0,3.0};
std::vector<double>v2{4.0,5.0};
std::cout<<v2[1]<<"\n";
for(auto x : v2) std::cout<<x<<"\n";