#include <iostream>
#include <cstdlib>

template<typename T>
class vector {
    T *mas;
    unsigned int top;
    unsigned int capacity;
     
public:
vector(): top(0), capacity(0), mas(NULL);

~vector();

vector(const vector &rhs): top(rhs.top), capacity(rhs.capacity);

vector& operator=(const vector & rhs);
	
vector(vector && rhs);

vector& operator=(vector && rhs);

T& operator()(unsigned row);
T operator()(unsigned row) const;
    
bool push_back(const T& d);

T pop_back();

bool resize( unsigned int new_capacity);

void shrink_to_fit();

void clear();
    
void print_vector();

};