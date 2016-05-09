#pragma once
#include <iostream>		// so that we can overload << and >>
#include <string>
using namespace std;

// Declarations for class Entry for a phone directory

class Product
{
	friend istream& operator >> (istream& a, Product& e);
	friend ostream& operator << (ostream& a, const Product& e);

public:
	Product();			// initializes all values to blanks
	string GetSKU();		// returns name in an entry
	string Save();
	void Load(string &line);

private:
	string SKU;		// A name is 20 characters,
	string Brand;	// so is a phone number,
	string Model;		// and so is an address.
	string Category;
	string Size;
	string Price;
	int Count;
};