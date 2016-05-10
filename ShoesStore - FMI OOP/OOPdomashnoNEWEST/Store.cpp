#include "stdafx.h"
#include "Store.h"
#include <fstream>
#include <iostream>
#include <cstring>		
#include "store.h"

using namespace std;

Store::Store()
{
	maxSize = 500;
    currentSize = 0;
    productList = new Product*[maxSize];
}

Store::~Store()
{
	for (int i = 0; i < currentSize; i++)
		delete productList[i];
	delete[] productList;
}

void Store::Insert()
{
	if (currentSize == maxSize)		
		Grow();

	cout << "\nType the sku, brand, model, category, size, price followed"
		<< "\n by RETURN or ENTER:\n> ";
	productList[currentSize] = new Product();
	cin >> *productList[currentSize];
	currentSize++;
}

void Store::Lookup() const
{
	
	string aSKU;
	cout << "\tType the sku to be looked up, followed by <Enter>: ";
	getline(cin,aSKU);

	int thisEntry = FindName(aSKU);	

	if (thisEntry == -1)
		cout << aSKU << " not found in current store\n";
	else
	{
		cout << "\nProduct found: ";
		cout << *productList[thisEntry];	
	}
}

void Store::Remove()
{
	string aSKU;
	cout << "\nType sku to be removed, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);	// Locate the sku in the store.

	if (thisEntry == -1)
		cout << aSKU << " not found in store";
	else
	{
		
		for (int j = thisEntry + 1; j < currentSize; j++)
			productList[j - 1] = productList[j];

		currentSize--;		
		cout << "Product removed.\n";
	}
}

void Store::Update()
{
	cout << "\nPlease enter the sku of the entry to be modified: ";
	string aSKU;
	getline(cin, aSKU);

	int thisProduct = FindName(aSKU);

	if (thisProduct == -1)
		cout << aSKU << " not found in current store\n";
	else
	{
		cout << "\nCurrent product is: \n";
		cout << *productList[thisProduct];		

		cout << "\nReplace with new product as follows: \n";
		cin >> *productList[thisProduct];		
	}
}

void Store::DisplayStore() const
{
	if (currentSize == 0)
	{
		cout << "\nCurrent store is empty.\n";
		return;
	}
	cout << "\n\t***SKU***BRAND***MODEL***CATEGORY***SIZE***PRICE\n\n";

	for (int i = 0; i < currentSize; i++)
	{
		cout<<*productList[i];
	}
}

void Store::Grow()
{
	maxSize = currentSize + 500;			
	Product** newList = new Product*[maxSize];

	for (int i = 0; i < currentSize; i++)	
		newList[i] = productList[i];		

	delete[] productList;			
	productList = newList;			
}

int Store::FindName(string aName) const
{
	for (int i = 0; i < currentSize; i++)	
		if (productList[i]->GetSKU().compare(aName) == 0)
			return i;		

	return -1;				
}
void Store::Save() const
{
	cout << "\nPlease enter the name of file to save to: ";
	string fName;
	getline(cin, fName);
	ofstream ofs(fName);

	// Display a header.
	ofs << "PRODUCTS IN THE STORE" << endl;

	for (int i = 0; i < currentSize; i++)	
	{
		ofs << productList[i]->Save()<<endl;
	}
	ofs.close();
	cout << "Store saved.\n";
}
void Store::Load()
{
	string fName;
	int i, len = this->currentSize;
	cout << "Please enter the name of file to load: ";
	cin >> fName;
	ifstream ifs(fName);
	for (int i = 0; i < len; i++)
	{
		delete this->productList[i];
	}
	this->currentSize = 0;
	string line;
	getline(ifs,line);
	i = 0;
	while (getline(ifs, line))
	{
		Product* product = new Product();
		product->Load(line);
		this->productList[this->currentSize++] = product;
	}
	ifs.close();
	cout << "Loaded." << endl;
}