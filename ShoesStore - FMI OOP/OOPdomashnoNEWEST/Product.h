#pragma once
#include <iostream>		
#include <string>
using namespace std;


class Product
{
	friend istream& operator >> (istream& a, Product& e);
	friend ostream& operator << (ostream& a, const Product& e);

public:
	Product();			
	string GetSKU();		
	string Save();
	void Load(string& line);
	string GetPrice();
	static void DecreaseCount();
private:
	string SKU;		
	string Brand;	
	string Model;		
	string Category;
	string Size;
	string Price;
	static int Count;
};