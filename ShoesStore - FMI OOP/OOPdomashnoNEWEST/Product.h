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
	Product();			
	string GetSKU();		
	string Save();
	void Load(string& line);
private:
	string SKU;		
	string Brand;	
	string Model;		
	string Category;
	string Size;
	string Price;
	int Count;
};