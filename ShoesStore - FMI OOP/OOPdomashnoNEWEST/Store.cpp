#include "stdafx.h"

#include "Store.h"

// Definitions for class Store
#include <fstream>
#include <iostream>
#include <cstring>		// for strcmp
#include "store.h"

using namespace std;

Store::Store()
// Set up empty store of products.
{
	maxSize = 5;
    currentSize = 0;
    productList = new Product*[maxSize];
}

Store::~Store()
// This destructor function for class Store
// deallocates the store's list of Product objects
{
	for (int i = 0; i < currentSize; i++)
		delete productList[i];
	delete[] productList;
}

void Store::Insert()
// Insert a new product into the store.
{
	if (currentSize == maxSize)		// If the store is full, grow it.
		Grow();

	cout << "\nType the name, phone number, and address, each followed"
		<< "\n by RETURN or ENTER:\n> ";
	productList[currentSize] = new Product();
	cin >> *productList[currentSize];	// read new product.
	currentSize++;
}

void Store::Lookup() const
//  Display the store product for a sku.
{
	// Prompt the user for a sku to be looked up
	string aSKU;
	cout << "\tType the sku to be looked up, followed by <Enter>: ";
	getline(cin,aSKU);

	int thisEntry = FindName(aSKU);	// Locate the sku in the directory.

	if (thisEntry == -1)
		cout << aSKU << " not found in current store\n";
	else
	{
		cout << "\nProduct found: ";
		cout << *productList[thisEntry];	// display product.
	}
}

void Store::Remove()
// Remove a product from the store.
{
	// Prompt the user for the sku to be removed.
	string aSKU;
	cout << "\nType sku to be removed, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);	// Locate the sku in the store.

	if (thisEntry == -1)
		cout << aSKU << " not found in store";
	else
	{
		// Shift each succeding element "down" one position in the
		// Store array, thereby deleting the desired entry.
		for (int j = thisEntry + 1; j < currentSize; j++)
			productList[j - 1] = productList[j];

		currentSize--;		// Decrement the current number of products.
		cout << "Entry removed.\n";
	}
}

void Store::Update()
// Update an existing store product by reentering
// each of its values.
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
		cout << *productList[thisProduct];		// Display the current product.

		cout << "\nReplace with new product as follows: \n";
		cin >> *productList[thisProduct];		// Get new values for product.
	}
}

void Store::DisplayDirectory() const
// Display the current store products
// on the standard output (the screen).
{
	if (currentSize == 0)
	{
		cout << "\nCurrent store is empty.\n";
		return;
	}

	// Display a header.
	cout << "\n\t***SKU***BRAND***MODEL***CATEGORY***SIZE***PRICE\n\n";

	for (int i = 0; i < currentSize; i++)	// For each product,
		cout << *productList[i];			// send it to output
}

void Store::Grow()
// Double the size of the store's entry list
// by creating a new, larger array of products
// and changing the store's pointer to refer to
// this new array.
{
	maxSize = currentSize + 5;			// Determine a new size.
	Product** newList = new Product*[maxSize];		// Allocate a new array.

	for (int i = 0; i < currentSize; i++)	// Copy each entry into
		newList[i] = productList[i];		// the new array.

	delete[] productList;			// Remove the old array
	productList = newList;			// Point old name to new array.
}

int Store::FindName(string aName) const
// Locate a sku in the store.  Returns the
// position of the product list as an integer if found.
// and returns -1 if the product is not found in the store.
{
	for (int i = 0; i < currentSize; i++)	// Look at each entry.
		if (productList[i]->GetSKU().compare(aName) == 0)
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
	ofs << "PRODUCTS IN THE STORE" << endl;

	for (int i = 0; i < currentSize; i++)	// For each entry,
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