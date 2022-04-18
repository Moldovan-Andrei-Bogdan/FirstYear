#pragma once
//DO NOT INCLUDE SORTEDBAGITERATOR
#include <vector>

//DO NOT CHANGE THIS PART
typedef int TComp;
typedef TComp TElem;

typedef bool(*Relation)(TComp, TComp);

#define NULL_TCOMP -11111;

class SortedBagIterator;

class SortedBag {
    friend class SortedBagIterator;

private:
    //TODO - Representation
    std::vector<std::pair<int,int>> *elems;
    std::vector<std::pair<int, int>> *PrevAndNext;
    int head;
    int tail;
    int number_of_elements;
    Relation rel;

    std::vector<int> auxiliary_search(TComp elem);
    std::vector<int> auxiliary_search2(TComp elem);

public:
    //constructor
    SortedBag(Relation r);

    //adds an element to the sorted bag
    void add(TComp e);

    //removes one occurence of an element from a sorted bag
    //returns true if an eleent was removed, false otherwise (if e was not part of the sorted bag)
    bool remove(TComp e);

    //checks if an element appearch is the sorted bag
    bool search(TComp e) const;

    //returns the number of occurrences for an element in the sorted bag
    int nrOccurrences(TComp e) const;

    //returns the number of elements from the sorted bag
    int size() const;

    void print_list();

    void print_list_reverse();

    //returns an iterator for this sorted bag
    SortedBagIterator iterator() const;

    //checks if the sorted bag is empty
    bool isEmpty() const;

    void addOccurences(int nr, TComp elem);

    void update_positions();

    //destructor
    ~SortedBag();
};