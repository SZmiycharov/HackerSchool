#include "stdafx.h"

#include <sstream>

#pragma warning(disable : 4996)
#include <string>
#include <cstring>			
#include "Product.h"			

//---------- Operator Overloads ---------

istream& operator >> (istream& s, Product& e)
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
{
	s << '\t' << e.SKU;		
	s << '\t' << e.Brand;	
	s << '\t' << e.Model;	
	s << '\t' << e.Category;
	s << '\t' << e.Size;	
	s << '\t' << e.Price;	
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

string Product::GetPrice()
{
	return Price;
}
int Product::Count = 0;

void Product::DecreaseCount()
{
	Count--;
}






