#include "stdafx.h"

#include "Store.h"

// Definitions for class Store

#include <iostream>
#include <cstring>		// for strcmp
#include <fstream>
#include "store.h"

using namespace std;

Store::Store()
// Set up empty Store of products.
{
}

Store::~Store()
// This destructor function for class Store
// deallocates the store's list of Product objects
{
	for (int i = 0; i < productList.size(); i++)
		delete productList[i];
}

Store::Store(const Store & dir)
{
	productList.resize(dir.productList.size());
	for (int i = 0; i < dir.productList.size(); i++)
		productList[i] = new Product(*dir.productList[i]);
}

Store & Store::operator=(const Store & dir)
{
	if (this != &dir) {
		for (int i = 0; i < productList.size(); i++)
			delete productList[i];
		productList.resize(dir.productList.size());
		for (int i = 0; i < dir.productList.size(); i++)
			productList[i] = new Product(*dir.productList[i]);
	}
	return *this;
}

void Store::Insert()
// Insert a new product into the Store.
{

	cout << "\nType the sku, brand, model, category, size and price each followed"
		<< "\n by RETURN or ENTER:\n> ";
	Product* pProduct = new Product();
	cin >> *pProduct;	// read new product.
	productList.push_back(pProduct);
}

void Store::Lookup() const
//  Display the store product for a name.
{
	// Prompt the user for a sku to be looked up
	string aSKU;
	cout << "\tType the sku to be looked up, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);	// Locate the sku in the directory.

	if (thisEntry == -1)
		cout << aSKU << " not found in current directory\n";
	else
	{
		cout << "\nEntry found: ";
		cout << *productList[thisEntry];	// display product.
	}
}

void Store::Remove()
// Remove a product from the store.
{
	// Prompt the user for the sku to be removed.
	string aSKU;
	cout << "\nType sku of product to be removed, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);	// Locate the name in the directory.

	if (thisEntry == -1)
		cout << aSKU << " not found in directory";
	else
	{
		productList.erase(productList.begin() + thisEntry);
		cout << "Product removed.\n";
	}
}

void Store::Update()
// Update an existing store product by reentering
// each of its values (sku, brand, model, category, size and price).
{
	cout << "\nPlease enter the sku of the product to be modified: ";
	string aSKU;
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);

	if (thisEntry == -1)
		cout << aSKU << " not found in current directory\n";
	else
	{
		cout << "\nCurrent product is: \n";
		cout << *productList[thisEntry];		// Display the current entry.

		cout << "\nReplace with new products as follows: \n";
		cin >> *productList[thisEntry];		// Get new values for entry.
	}
}

void Store::DisplayDirectory() const
// Display the current directory entries
// on the standard output (the screen).
{
	if (productList.size() == 0)
	{
		cout << "\nCurrent store is empty.\n";
		return;
	}

	// Display a header.
	cout << "\n\t***SKU***BRAND***MODEL***CATEGORY***SIZE***PRICE\n\n";

	for (int i = 0; i < productList.size(); i++)	// For each entry,
		cout << *productList[i];			// send it to output
}


int Store::FindName(string aSKU) const
// Locate a sku in the store.  Returns the
// position of the product list as an integer if found.
// and returns -1 if the product is not found in the store.
{
	for (int i = 0; i < productList.size(); i++)	// Look at each product.
		if (productList[i]->GetSKU().compare(aSKU) == 0)
			return i;		// If found, return position and exit.

	return -1;				// Return -1 if never found.
}

void Store::Save() const
{
	cout << "\nPlease enter the name of file to save to: ";
	string fName;
	getline(cin, fName);
	ofstream ofs(fName);

	// Display a header.
	ofs << "SKU;BRAND;MODEL;CATEGORY;SIZE;PRICE;" << endl;

	for (int i = 0; i < productList.size(); i++)	// For each product
	{
		ofs << productList[i]->Save() << endl;
	}
	ofs.close();
	cout << "Store saved.\n";
}

void Store::Load()
{
	cout << "\nPlease enter the name of file to load: ";
	string fName;
	getline(cin, fName);
	ifstream ifs(fName);
	for (int i = 0; i < productList.size(); i++)
		delete productList[i];
	productList.resize(0);
	string line;
	// Get Header line
	getline(ifs, line);
	while (getline(ifs, line))
	{
		Product *pProduct = new Product();
		pProduct->Load(line);
		productList.push_back(pProduct);
	}
	ifs.close();
	cout << "Directory loaded.\n";
}