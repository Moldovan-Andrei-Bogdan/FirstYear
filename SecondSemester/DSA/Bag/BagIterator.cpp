#include <exception>
#include "BagIterator.h"
#include "Bag.h"
#include <exception>
using namespace std;


BagIterator::BagIterator(const Bag& c) : bag(c)
{
	this->index_elements = 0;
}

void BagIterator::first() {
	//TODO - Implementation
	this->index_elements = 0;
}


void BagIterator::next() {
	//TODO - Implementation
	if (this->index_elements  == this->bag.length_of_positions_array) {
		throw exception();
	}
	else {
		this->index_elements += 1;
	}
}


bool BagIterator::valid() const {
	//TODO - Implementation
	if (this->index_elements <= this->bag.length_of_positions_array - 1) {
		return true;
	}
	return false;
}



TElem BagIterator::getCurrent() const
{
	//TODO - Implementation
	if (this->index_elements == this->bag.length_of_positions_array) {
		throw exception();
	}
	return this->bag.unique_array[this->bag.positions_array[this->index_elements]];
}
