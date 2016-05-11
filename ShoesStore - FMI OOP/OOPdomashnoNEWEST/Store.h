#pragma once
#include "Product.h"
#include <vector>

class Store
{
public:
	Store();			
	~Store();		
	void Insert();		
	void Lookup() const;
	void Remove();		
	void Update();		
	void DisplayStore() const;
	void Save() const;        
	void Load();              
private:
	int	maxSize,		
		currentSize;		
	Product** productList;		
	void Grow();
	int FindName(string aSKU) const;	
};
