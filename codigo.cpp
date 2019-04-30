#include<cmath>
#include <iostream>
#include <fstream>
#include<vector>
using namespace std;



int max = 101;
int min = -100;

double x = ((double) rand() / (RAND_MAX));
ofstream myfile;
double PI = 3.141592;



double distnormal(double x);


int main(){
myfile.open("MetHas.txt");
if (myfile.is_open())
    {   
    
    for(cont = 0;cont<Nit;cont++){
     
     double propuesta = x+ 2*((double) rand() / (RAND_MAX))-1;
     double F_actual=distnormal(x);
     double F_propuesta=distnormal(propuesta);
     
