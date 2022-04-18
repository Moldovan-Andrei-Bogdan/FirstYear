#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <vector>
#include <iostream>

SortedBag::SortedBag(Relation r) {
    this->elems = new std::vector<std::pair<int, int>>;
    this->PrevAndNext = new std::vector<std::pair<int, int>>;
    this->head = -1;
    this->tail = -1;
    this->rel = r;
    this->number_of_elements = 0;
}

void SortedBag::add(TComp e) {
    /// BC=Theta(1) AC=WC=Theta(number of nodes in list)
    if (this->number_of_elements == 0) {
        (*this->elems).push_back(std::make_pair(e, 1));
        (*this->PrevAndNext).push_back(std::make_pair(-1, -1));
        this->head = 0;
        this->tail = 0;
        this->number_of_elements += 1;
    } else {
        std::vector<int> search_result = this->auxiliary_search(e);
        if (search_result[0] == -400) {
            (*this->elems)[search_result[1]].second += 1;
            this->number_of_elements += 1;
        } else if (search_result[0] == -100) {
            (*this->elems).push_back(std::make_pair(e, 1));
            (*this->PrevAndNext).push_back(std::make_pair(this->tail, -1));
            this->number_of_elements += 1;
            (*this->PrevAndNext)[this->tail].second = (*this->elems).size() - 1;
            this->tail = (*this->elems).size() - 1;
        } else if (search_result[0] == -200) {
            (*this->elems).push_back(std::make_pair(e, 1));
            (*this->PrevAndNext).push_back(std::make_pair(-1, this->head));
            this->number_of_elements += 1;
            (*this->PrevAndNext)[this->head].first = (*this->elems).size() - 1;
            this->head = (*this->elems).size() - 1;
        } else if (search_result[0] == -300) {
            this->number_of_elements += 1;
            (*this->elems).push_back(std::make_pair(e, 1));
            (*this->PrevAndNext).push_back(
                    std::make_pair((*this->PrevAndNext)[search_result[1]].first, search_result[1]));
            (*this->PrevAndNext)[(*this->PrevAndNext)[search_result[1]].first].second = (*this->elems).size() - 1;
            (*this->PrevAndNext)[search_result[1]].first = (*this->elems).size() - 1;
        }
    }
}

bool SortedBag::remove(TComp e) {
    /// BC=Theta(1) AC=WC=Theta(number of nodes in list)
    if (this->number_of_elements == 0) {
        return false;
    } else {
        std::vector<int> search_result = this->auxiliary_search2(e);
        if (search_result[0] == -400) {
            (*this->elems)[search_result[1]].second -= 1;
            if ((*this->elems)[search_result[1]].second == 0) {
                if ((*this->PrevAndNext)[search_result[1]].first == -1) {
                    (*this->PrevAndNext)[(*this->PrevAndNext)[search_result[1]].second].first = -1;
                    this->head = (*this->PrevAndNext)[search_result[1]].second;
                } else if ((*this->PrevAndNext)[search_result[1]].second == -1) {
                    (*this->PrevAndNext)[(*this->PrevAndNext)[search_result[1]].first].second = -1;
                    this->tail = (*this->PrevAndNext)[search_result[1]].first;
                } else {
                    (*this->PrevAndNext)[(*this->PrevAndNext)[search_result[1]].first].second = (*this->PrevAndNext)[search_result[1]].second;
                    (*this->PrevAndNext)[(*this->PrevAndNext)[search_result[1]].second].first = (*this->PrevAndNext)[search_result[1]].first;
                }
            }
            this->number_of_elements -= 1;
            return true;
        } else {
            return false;
        }
    }
}

std::vector<int> SortedBag::auxiliary_search(TComp elem) {
    ///BC=Theta(1) AC=WC=Theta(number of nodes in list)
    int itr;
    itr = this->head;
    while (itr != -1 && this->rel((*this->elems)[itr].first, elem) && (*this->elems)[itr].first != elem) {
        itr = (*this->PrevAndNext)[itr].second;
    }
    std::vector<int> values_to_return;
    if ((*this->elems)[itr].first == elem && itr != -1) {
        values_to_return.push_back(-400);
        values_to_return.push_back(itr);
        return values_to_return;
    } else if (itr == -1) {
        values_to_return.push_back(-100);
        return values_to_return;
    } else if ((*this->PrevAndNext)[itr].first == -1 && itr != -1) {
        values_to_return.push_back(-200);
        values_to_return.push_back(itr);
        return values_to_return;
    } else {
        values_to_return.push_back(-300);
        values_to_return.push_back(itr);
        return values_to_return;
    }
}

std::vector<int> SortedBag::auxiliary_search2(TComp elem) {
    ///BC=Theta(1) AC=WC=Theta(number of nodes in list)
    int itr;
    itr = this->head;
    while (itr != -1 && (*this->elems)[itr].first != elem) {
        itr = (*this->PrevAndNext)[itr].second;
    }
    std::vector<int> values_to_return;
    if (itr == -1) {
        values_to_return.push_back(-200);
        values_to_return.push_back(itr);
        return values_to_return;
    } else if ((*this->elems)[itr].first == elem) {
        values_to_return.push_back(-400);
        values_to_return.push_back(itr);
        return values_to_return;
    }
}


bool SortedBag::search(TComp elem) const {
    ///BC=Theta(1) AC=WC=Theta(number of nodes in list)
    int itr;
    itr = this->head;
    while (itr != -1 && (*this->elems)[itr].first != elem) {
        itr = (*this->PrevAndNext)[itr].second;
    }
    if (itr == -1) {
        return false;
    } else if ((*this->elems)[itr].first == elem) {
        return true;
    }
}


int SortedBag::nrOccurrences(TComp elem) const {
    ///BC=Theta(1) AC=WC=Theta(1)
    int itr;
    itr = this->head;
    while (itr != -1 && (*this->elems)[itr].first != elem) {
        itr = (*this->PrevAndNext)[itr].second;
    }
    if (itr == -1) {
        return 0;
    } else if ((*this->elems)[itr].first == elem) {
        return (*this->elems)[itr].second;
    }
}


int SortedBag::size() const {
    /// AC=BC=WC=Theta(1)
    return this->number_of_elements;
}


bool SortedBag::isEmpty() const {
    /// AC=BC=WC=Theta(1)
    if (this->number_of_elements == 0) {
        return true;
    }
    return false;
}


SortedBagIterator SortedBag::iterator() const {
    ///AC=BC=WC=Theta(1)
    return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
    delete this->elems;
    delete this->PrevAndNext;
}

void SortedBag::addOccurences(int nr, TComp elem) {
    /// BC=Theta(1) AC=WC=Theta(number of nodes in the list)
    if (elem < 0) {
        throw std::exception();
    } else {
        std::vector<int> src_result;
        src_result=this->auxiliary_search(elem);
        if(src_result[0]==-400){
            (*this->elems)[src_result[1]].second += nr;
            this->number_of_elements+=nr;
        }else if(src_result[0]==-100){
            (*this->elems).push_back(std::make_pair(elem, nr));
            (*this->PrevAndNext).push_back(std::make_pair(this->tail, -1));
            this->number_of_elements += nr;
            (*this->PrevAndNext)[this->tail].second = (*this->elems).size() - 1;
            this->tail = (*this->elems).size() - 1;
        }else if(src_result[0]==-200){
            (*this->elems).push_back(std::make_pair(elem, nr));
            (*this->PrevAndNext).push_back(std::make_pair(-1, this->head));
            this->number_of_elements += nr;
            (*this->PrevAndNext)[this->head].first = (*this->elems).size() - 1;
            this->head = (*this->elems).size() - 1;
        }else if(src_result[0]==-300){
            this->number_of_elements += nr;
            (*this->elems).push_back(std::make_pair(elem, nr));
            (*this->PrevAndNext).push_back(
                    std::make_pair((*this->PrevAndNext)[src_result[1]].first, src_result[1]));
            (*this->PrevAndNext)[(*this->PrevAndNext)[src_result[1]].first].second = (*this->elems).size() - 1;
            (*this->PrevAndNext)[src_result[1]].first = (*this->elems).size() - 1;
        }
    }
}

void SortedBag::print_list() {
    /// AC=BC=WC=Theta(number of nodes in list)
    int itr;
    itr = this->head;
    while (itr != -1) {
        std::cout << (*this->elems)[itr].first << " ";
        itr = (*this->PrevAndNext)[itr].second;
    }
    std::cout << '\n';
}

void SortedBag::print_list_reverse() {
    /// AC=BC=WC=Theta(number of nodes in the list)
    int itr;
    itr = this->tail;
    while (itr != -1) {
        std::cout << (*this->elems)[itr].first << " ";
        itr = (*this->PrevAndNext)[itr].first;
    }
    std::cout << '\n';
}
