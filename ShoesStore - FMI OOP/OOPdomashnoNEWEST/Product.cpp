#include "stdafx.h"

#include <sstream>

#pragma warning(disable : 4996)
#include <string>
#include <cstring>			
#include "Product.h"			

//---------- Operator Overloads ---------

istream& operator >> (istream& s, Product& e)
// read in data through overloaded >> operator
{
	getline(s, e.SKU);		// Gets a name; discards newline.
	getline(s, e.Brand);	// Gets a phone; discards newline.
	getline(s, e.Model);		// Gets an address; discards newline.
	getline(s, e.Category);
	getline(s, e.Size);
	getline(s, e.Price);

	return s;
}

ostream& operator << (ostream& s, const Product& e)
// print an entry using the overloaded << operator
{
	s << '\t' << e.SKU;		// Display name (after tabbing).
	s << '\t' << e.Brand;		// Display phone number.
	s << '\t' << e.Model;		// Display phone number.
	s << '\t' << e.Category;		// Display phone number.
	s << '\t' << e.Size;		// Display phone number.
	s << '\t' << e.Price;			// Display address.
	s << '\n';

	return s;
}

//---------- Member functions ----------

Product::Product() : SKU(""), Brand(""), Model(""), Category(""), Size(""), Price("")
{
	Count++;
}

string Product::GetSKU()
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







