#include <iostream>

struct subforwardlist {
     int data;
     subforwardlist* next;
};

bool init(subforwardlist **sfl);
bool push_back(subforwardlist **sfl, int d);
int pop_back(subforwardlist *sfl);
bool push_forward(subforwardlist **sfl, int d);	
int pop_forward(subforwardlist **sfl);
bool push_where(subforwardlist *sfl, unsigned int where, int d); //добавление элемента с порядковым номером where		
int erase_where(subforwardlist *sfl, unsigned int where);	//удаление элемента с порядковым номером where, если пустой - возвращать 0

unsigned int size(subforwardlist  **sfl);	//определить размер недосписка

void clear(subforwardlist  **sfl);	//очистить содержимое недосписка

bool init(subforwardlist **sfl){
*sfl = NULL;
return 1;
}

bool push_back(subforwardlist **sfl, int d){
while ((*sfl) != NULL)
    sfl = &((*sfl) -> next);
subforwardlist* new_sfl = new subforwardlist;
if (new_sfl == NULL){return 0;}
(*sfl) = new_sfl;
new_sfl -> data = d;
new_sfl -> next = NULL;
return 1;
}

void print_list(subforwardlist **sfl){
while ((*sfl) != NULL){
    std::cout<< (*sfl) -> data <<std::endl;
    sfl = &((*sfl) -> next);
}
}

int pop_back(subforwardlist **sfl){
if (*sfl == NULL){return 0;}
while ((*sfl) -> next != NULL)
    sfl = &((*sfl) -> next);
int d = (*sfl) -> data;
delete (*sfl);
(*sfl) = NULL;
return d;
}

bool push_forward(subforwardlist **sfl, int d){
subforwardlist* new_sfl = new subforwardlist;
if (new_sfl == NULL){return 0;}
new_sfl -> data = d;
new_sfl -> next = *sfl;
*sfl = new_sfl;
return 1;
}

int pop_forward(subforwardlist **sfl){
if (*sfl == NULL){return 0;}
int d = (*sfl) -> data;
subforwardlist* nsfl = (*sfl) -> next;
delete (*sfl);
*sfl = nsfl;
return d;
}

bool push_where(subforwardlist **sfl, unsigned int where, int d){
subforwardlist* new_sfl = new subforwardlist;
if (new_sfl == NULL){return 0;}
int gg = 0;
if (where == 0){
    push_forward(sfl, d);
    return 1;
}
for (unsigned int i = 0; i < where - 1; i++)
    sfl = &((*sfl) -> next);
    gg++;
    if ((*sfl) == NULL and gg < where){
        delete new_sfl;
        return 0;
    }
new_sfl -> data = d;
new_sfl -> next = (*sfl) -> next;
(*sfl) -> next = new_sfl;
return 1;
}

int erase_where(subforwardlist **sfl, unsigned int where){
if (sfl == NULL){return 0;}
int gg = 0;
if (where == 0){
    return pop_forward(sfl);
}
for (unsigned int i = 0; i < where - 1; i++)
    sfl = &((*sfl) -> next);
    gg++;
    if ((*sfl) == NULL and gg < where){
        return 0;
    }
int d = ((*sfl)-> next) -> data;
subforwardlist* new_sfl = ((*sfl)-> next) -> next;
delete (*sfl)-> next;
(*sfl) -> next = new_sfl;
return d;
}

unsigned int size(subforwardlist  **sfl){
int size = 0;
while ((*sfl) != NULL){
    size++;
    sfl = &((*sfl) -> next);
}
return size;
}

void clear(subforwardlist **sfl){
while (*sfl != NULL){
    subforwardlist* nsfl = (*sfl) -> next;
    delete (*sfl);
    *sfl = nsfl;
}
}

int main()
{
subforwardlist* f = new subforwardlist;
subforwardlist** e = &f;
init(e);
push_back(e, 3);
push_back(e, 3);
push_back(e, 4);
print_list(e);
std::cout<<" "<<std::endl;
int z = pop_back(e);
print_list(e);
std::cout<< z <<"-pop_back"<<std::endl;
std::cout<<" "<<std::endl;
push_forward(e, 2);
print_list(e);
std::cout<<" "<<std::endl;
int r = pop_forward(e);
std::cout<< r <<"-pop_forward"<<std::endl;
print_list(e);
std::cout<<" "<<std::endl;
push_where(e, 2, 8);
print_list(e);
std::cout<<" "<<std::endl;
int d = erase_where(e, 1);
std::cout<< d <<"-pop_where"<<std::endl;
print_list(e);
std::cout<<" "<<std::endl;
int s = size(e);
std::cout<<"size: "<<s<<std::endl;
clear(e);
int ss = size(e);
std::cout<<"size: "<<ss<<std::endl;
print_list(e);
push_back(e, 3);
push_back(e, 3);
push_back(e, 4);
print_list(e);
int sss = size(e);
std::cout<<"size: "<<sss<<std::endl;
return 0;
}

