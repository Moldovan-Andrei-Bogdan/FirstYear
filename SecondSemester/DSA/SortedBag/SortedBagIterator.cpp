#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag &b) : bag(b) {
    this->head_of_dll = this->bag.head;
    this->tail_of_dll = this->bag.tail;
    this->aux = head_of_dll;
    this->number_of_elements_of_dll = this->bag.number_of_elements;
    this->count_of_elem = 0;
}

TComp SortedBagIterator::getCurrent() {
    if (this->aux == -1) {
        throw std::exception();
    } else {
        return (*this->bag.elems)[this->head_of_dll].first;
    }
}

bool SortedBagIterator::valid() {
    if (this->aux == -1) {
        return false;
    }
    return true;
}

void SortedBagIterator::next() {
    if (this->aux == -1) {
        throw std::exception();
    } else {
        if (this->count_of_elem + 1 < (*this->bag.elems)[this->aux].second) {
            this->count_of_elem += 1;
        } else if (this->count_of_elem + 1 == (*this->bag.elems)[this->aux].second) {
            this->aux = (*this->bag.PrevAndNext)[this->aux].second;
            this->count_of_elem = 0;
        }
    }
}

void SortedBagIterator::first() {
    this->head_of_dll = this->bag.head;
    this->aux=this->bag.head;
}

