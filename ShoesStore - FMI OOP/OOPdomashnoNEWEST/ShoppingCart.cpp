#include "stdafx.h"
#include "ShoppingCart.h"
#include <fstream>
#include <iostream>
#include <cstring>		
#include "ShoppingCart.h"
#include "Product.h"

using namespace std;

ShoppingCart::ShoppingCart()
{
	maxSize = 500;
	currentSize = 0;
	shoppingList = new Product*[maxSize];
}

ShoppingCart::~ShoppingCart()
{
	for (int i = 0; i < currentSize; i++)
		delete shoppingList[i];
	delete[] shoppingList;
}

void ShoppingCart::Insert()
{
	if (currentSize == maxSize)
		Grow();

	cout << "\nType the sku, brand, model, category, size, price followed"
		<< "\n by RETURN or ENTER:\n> ";
	shoppingList[currentSize] = new Product();
	cin >> *shoppingList[currentSize];
	currentSize++;
}

void ShoppingCart::Lookup() const
{

	string aSKU;
	cout << "\tType the sku to be looked up, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);

	if (thisEntry == -1)
		cout << aSKU << " not found in current shopping cart\n";
	else
	{
		cout << "\nProduct found: ";
		cout << *shoppingList[thisEntry];
	}
}

void ShoppingCart::Remove()
{
	string aSKU;
	cout << "\nType sku to be removed, followed by <Enter>: ";
	getline(cin, aSKU);

	int thisEntry = FindName(aSKU);	// Locate the sku in the store.

	if (thisEntry == -1)
		cout << aSKU << " not found in shopping cart";
	else
	{

		for (int j = thisEntry + 1; j < currentSize; j++)
			shoppingList[j - 1] = shoppingList[j];

		currentSize--;
		cout << "Product removed.\n";
	}
}



void ShoppingCart::DisplayCart() const
{
	if (currentSize == 0)
	{
		cout << "\nCurrent cart is empty.\n";
		return;
	}
	cout << "\n\t***SKU***BRAND***MODEL***CATEGORY***SIZE***PRICE\n\n";

	for (int i = 0; i < currentSize; i++)
	{
		cout << *shoppingList[i];
	}
}

void ShoppingCart::Grow()
{
	maxSize = currentSize + 500;
	Product** newList = new Product*[maxSize];

	for (int i = 0; i < currentSize; i++)
		newList[i] = shoppingList[i];

	delete[] shoppingList;
	shoppingList = newList;
}

int ShoppingCart::FindName(string aName) const
{
	for (int i = 0; i < currentSize; i++)
		if (shoppingList[i]->GetSKU().compare(aName) == 0)
			return i;

	return -1;
}
void ShoppingCart::Save() const
{
	cout << "\nPlease enter the name of file to save to: ";
	string fName;
	getline(cin, fName);
	ofstream ofs(fName);

	// Display a header.
	ofs << "PRODUCTS IN THE SHOPPING CART" << endl;

	for (int i = 0; i < currentSize; i++)
	{
		ofs << shoppingList[i]->Save() << endl;
	}
	ofs.close();
	cout << "Shopping cart saved.\n";
}
void ShoppingCart::Load()
{
	string fName;
	int i, len = this->currentSize;
	cout << "Please enter the name of file to load: ";
	cin >> fName;
	ifstream ifs(fName);
	for (int i = 0; i < len; i++)
	{
		delete this->shoppingList[i];
	}
	this->currentSize = 0;
	string line;
	getline(ifs, line);
	i = 0;
	while (getline(ifs, line))
	{
		Product* product = new Product();
		product->Load(line);
		this->shoppingList[this->currentSize++] = product;
	}
	ifs.close();
	cout << "Loaded." << endl;
}
void ShoppingCart::Checkout()
{
	if (currentSize == 0)
	{
		cout << "\nCurrent shopping cart is empty.\n";
		return;
	}
	cout << "\n\t***PRODUCTS YOU BOUGHT***\n\n";

	int price = 0;

	for (int i = 0; i < currentSize; i++)
	{
		cout << *shoppingList[i];
		price += atoi(shoppingList[i]->GetPrice().c_str());
		Product::DecreaseCount();
	}
	cout <<"Cost of all products: " <<price;
}