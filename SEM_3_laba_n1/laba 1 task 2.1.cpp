#include <iostream>
void my_sort(int n, int* array);
void swapswap(int a, int b, int* ar){
    int c = ar[a];
    ar[a] = ar[b];
    ar[b] = c;
}

void sift_down(int n, int ver, int* array){
while (2*ver + 1 <= n-1){
    int u = 2*ver + 1;
    if (2*ver + 2 <= n-1 and array[ver * 2 + 2] > array[ver * 2 + 1]){
        u = 2*ver + 2;
        }
    if (array[u] > array[ver]){
        swapswap(u, ver, array);
        ver = u;
    }
    else break;
}}

void heapify(int n, int* array){
for (int i=n-1; i>=0; --i){
    sift_down(n, i, array);
}}

void extract_max(int* n, int* array){
swapswap(0, *(n)-1, array);
*n = *(n)-1;
sift_down(*n, 0, array);
}

void my_sort(int n, int* array){
    heapify(n, array);
    int f = n;
    for (int k = 0; k<f; k++){
        extract_max(&n, array);
}
}

int main(){
    int n = 20;
    int *a = new int[n];
    for (int i=0; i<n; i++){
        a[i] = rand() % 100 + 1;
    }
    for (int i=0; i<n; i++){
        std::cout<< a[i]<<" ";
    }
    std::cout<<std::endl;
    my_sort(n, a);
    for (int i=0; i<n; i++){
        std::cout<< a[i]<<" ";
    }
    return 0;
}

