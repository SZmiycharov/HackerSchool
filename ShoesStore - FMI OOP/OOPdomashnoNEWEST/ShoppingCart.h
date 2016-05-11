#pragma once
// Declarations for class Directory, where a directory
// is a collection of Entries, declared in "ENTRY.H".

#include "Product.h"
#include <vector>

class ShoppingCart
{
public:
	ShoppingCart();		
	~ShoppingCart();	
	void Insert();		 
	void Lookup() const;
	void Remove();		
	void DisplayCart() const;	
	void Save() const;             
	void Load();                   
	void Checkout();
private:
	int	maxSize,		
		currentSize;		
	Product** shoppingList;		
	void Grow();
	int FindName(string aSKU) const;	
};
