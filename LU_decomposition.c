//Sagar Dam
// DNAP
/* Due to a problem (occured due to some update) in my machine I can't run any c file in my computer. 
 There is no such problem in python. So for this code, I only borrowed it from one of my friends. 
 I will submit my own code after I get resolved from that. I only had gone through this code and checked
 the functions of the GSL codes. 
 
 	Sorry for the inconvenience. I will upload my own c code later.*/

#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_linalg.h>

int main()
{
  float A_data[]={1,0.67,0.33,0.45,1,0.55,0.67,0.33,1};
  float b_data[]={2,2,2};
  gsl_matrix_view A=gsl_matrix_view_array(A_data,3,3);
  gsl_vector_view b=gsl_vector_view_array(b_data,3);
  gsl_vector *x=gsl_vector_alloc(3);
  int s;
  gsl_permutation *p=gsl_permutation_alloc(3);
  gsl_linalg_LU_decomp(&A.matrix,p,&s);
  gsl_linalg_LU_solve(&A.matrix,p,&b.vector,x);
  gsl_vector_fprintf(stdout,x,"%g \n");
  gsl_permutation_free(p);
  gsl_vector_free(x);
  return 0;
}
