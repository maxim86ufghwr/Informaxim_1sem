#include <iostream>
#include <cstdlib>
#include "vector.hpp"

template<typename T>
class vector {
    T *mas;
    unsigned int top;
    unsigned int capacity;
     
public:
vector(): top(0), capacity(0), mas(NULL){}

~vector(){
    delete[] mas;
    mas = NULL;
}

vector(const vector &rhs): top(rhs.top), capacity(rhs.capacity){
    mas = new T[capacity];
    for (int i = 0; i < top ; i++)
        mas[i] = rhs.mas[i];
}

vector& operator=(const vector & rhs){
	if (this == &rhs) return *this;
	top = rhs.top;
    capacity = rhs.capacity;
	delete mas;
	mas = new T[capacity];
	for (int i = 0; i < top ; i++)
        mas[i] = rhs.mas[i];
	return *this;
	}
	
vector(vector && rhs){
    top = rhs.top;
    capacity = rhs.capacity;
    mas = rhs.mas;
    rhs.top = 0;
    rhs.capacity = 0;
    rhs.mas = nullptr;
}

vector& operator=(vector && rhs){
    top = rhs.top;
    capacity = rhs.capacity;
    delete[] mas;
    mas = rhs.mas;
    rhs.top = 0;
    rhs.capacity = 0;
    rhs.mas = nullptr;
    return *this;
}

T& operator()(unsigned row) {
    return mas[row];
}
T operator()(unsigned row) const{
    return mas[row];
}
    
bool push_back(const T& d){
    if (capacity == top) {
    capacity = (capacity + 1) * 2;
    T* tm = new T[capacity];

    if (tm == NULL or (mas == NULL and top != 0) ){return 0;}

    for (int i = 0; i < (capacity - 1) / 2; i++)
        tm[i] = mas[i];
    
    delete [] mas;
    mas = tm;
    }
    mas[top++] = d;
    return 1;
}

T pop_back(){
    if (top == 0) return T();
    return mas[--top];
}

bool resize( unsigned int new_capacity){
    T* tm = new T[new_capacity];
    if (tm == NULL or (mas == NULL and top != 0)){return 0;}
    if (new_capacity > top){
        for (int i = 0; i < top; i++)
            tm[i] = mas[i];
        capacity = new_capacity;
    }
    else {
        for (int i = 0; i < new_capacity; i++)
            tm[i] = mas[i];
        capacity = new_capacity;
        top = new_capacity;
    }
    delete [] mas;
    mas = tm;
    return 1;
}

void shrink_to_fit(){
    T* tm = new T[top];
    for (int i = 0; i < top; i++)
        tm[i] = mas[i];

    delete [] mas;
    mas = tm;
    capacity = top;
    }

void clear(){
    top = 0;
    }
    
void print_vector(){
    std::cout << "capacity: " << capacity << " top: " << top << std::endl;
    for (unsigned int i = 0; i < top; i++)
    std::cout << mas[i] << std::endl;
    std::cout << "print_vector" << std::endl;
}

};