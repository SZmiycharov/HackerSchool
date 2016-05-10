#include "stdafx.h"

#include <sstream>

#pragma warning(disable : 4996)

// Definition of class Entry for a phone directory.
// Note that although we need iostream.h, we don't mention it here,
// since <iostream.h> is already included in "PRODUCT.H"

#include <cstring>			// for strlen, strcpy
#include "Product.h"			// for class Product

//---------- Operator Overloads ---------

istream& operator >> (istream& s, Product& e)
// read in data through overloaded >> operator
{
	getline(s, e.SKU);		
	getline(s, e.Brand);	
	getline(s, e.Model);
	getline(s, e.Category);
	getline(s, e.Size);
	getline(s, e.Price);	

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

Product::Product() : SKU(""), Brand(""), Model(""), Category(""), Size(""), Price("")
// This constructor for class Product initializes the sku, brand, model, category,
// size and price to be blank strings.
{
}

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

void Product::Load(string &line)
{
	stringstream sstream(line);

	getline(sstream, SKU, ';');		
	getline(sstream, Brand, ';');	
	getline(sstream, Model, ';');	
	getline(sstream, Category, ';');
	getline(sstream, Size, ';');
	getline(sstream, Price, ';');
}





