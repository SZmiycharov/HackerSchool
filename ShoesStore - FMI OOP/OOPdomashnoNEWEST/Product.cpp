#include "stdafx.h"

#include <sstream>

#pragma warning(disable : 4996)
#include <string>
#include <cstring>			// for strlen, strcpy
#include "Product.h"			// for class Product

//---------- Operator Overloads ---------

istream& operator >> (istream& s, Product& e)
// read in data through overloaded >> operator
{
	getline(s,e.SKU);
	getline(s,e.Brand);
	getline(s,e.Model);
	getline(s,e.Category);
	getline(s,e.Size);
	getline(s,e.Price);

	return s;
}

ostream& operator << (ostream& s, const Product& e)
// print an entry using the overloaded << operator
{
	int i;

	s << " " << e.SKU;

	s << " " << e.Brand;

	s << " " << e.Model;

	s << " " << e.Category;

	s << " " << e.Size;

	s << " " << e.Price;
	s << '\n';

	return s;
}

//---------- Member functions ----------

/*Product::Product() : SKU(""), Brand(""), Model(""), Category(""), Size(""), Price("")
// This constructor for class Entry initializes the name, phone number,
// and room number to be blank strings.
{
}*/

string Product::GetSKU()
// Return the SKU part of an entry.
{
	return SKU;
}

string Product::Save()
{
	string line = SKU + ";" + Brand + ";" + Model + ";" + Category + ";" + Size + ";" + Price;
	return line;
}
void Product::Load(string& line)
{
	string skuString, brandString, modelString, categoryString, sizeString, priceString;
	stringstream sstream(line);

	sstream.str();
	getline(sstream, skuString, ';');
	SKU = skuString;

	sstream.str();
	getline(sstream, brandString, ';');
	Brand = brandString;

	sstream.str();
	getline(sstream, modelString, ';');
	Model = modelString;

	sstream.str();
	getline(sstream, categoryString, ';');
	Category = categoryString;

	sstream.str();
	getline(sstream, sizeString, ';');
	Size = sizeString;

	sstream.str();
	getline(sstream, priceString, ';');
	Price = priceString;
}







