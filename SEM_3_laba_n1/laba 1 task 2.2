#include <iostream>
#include <time.h>
void my_sort(int n, int* array);
void merge(int* A, int* B, int* C, int f){
int i = 0;
int j = 0;
int p = 0;
while ((i < (f - f/2)) and (j < f/2)){
if (A[i] < B[j]){
    C[p++] = A[i++];
}
else{
    C[p++] = B[j++];
}
}
while (i < (f - f/2)){
C[p++] = A[i++];
}
while (j < f/2){
C[p++] = B[j++];
}
}

void my_sort(int n, int* array){
if (n==1){return;}
int *A = new int[n - n/2];
int *B = new int[n/2];
for (int i=0; i<(n-n/2); i++)
    A[i] = array[i];
for (int i=0; i<n/2; i++)
    B[i] = array[i + n - n/2];
my_sort((n - n/2), A);
my_sort(n/2, B);
merge(A, B, array, n);
delete[] A;
delete[] B;
}

int main(){
    clock_t start = clock();
    int n = 10;
    int *a = new int[n];
    for (int i=0; i<n; i++)
        a[i] = rand() % 100 + 1;
    //for (int i=0; i<n; i++)
        //std::cout<< a[i]<<" ";
    //std::cout<<std::endl;
    my_sort(n, a);
    //for (int i=0; i<n; i++)
        //std::cout<< a[i]<<" ";
    //std::cout<<std::endl;
    clock_t end = clock();
    double seconds = (double)(end - start) / CLOCKS_PER_SEC;
    std::cout<<seconds;
    return 0;
}
