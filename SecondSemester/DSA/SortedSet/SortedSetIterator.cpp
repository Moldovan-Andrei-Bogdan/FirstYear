#include "SortedSetIterator.h"
#include <exception>

using namespace std;

SortedSetIterator::SortedSetIterator(const SortedSet &m) : multime(m) {
    //TODO - Implementation
    this->node=this->multime.root;
}


void SortedSetIterator::first() {
    //TODO - Implementation
    this->node=this->multime.root;
}


void SortedSetIterator::next() {
    //TODO - Implementation
    if(this->node!= nullptr) {
        this->node = this->node->next;
    }else{
        throw std::exception();
    }
}


TElem SortedSetIterator::getCurrent() {
    //TODO - Implementation
    if(this->node!= nullptr) {
        return this->node->info;
    }else{
        throw std::exception();
    }
}

bool SortedSetIterator::valid() const {
    //TODO - Implementation
    if(this->node!= nullptr){
        return true;
    }
    return false;
}

