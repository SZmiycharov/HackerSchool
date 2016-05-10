#pragma once
// Declarations for class Directory, where a directory
// is a collection of Entries, declared in "ENTRY.H".

#include "Product.h"
#include <vector>

class Store
{
public:
	Store();			// Set up empty directory of entries
	~Store();		// Deallocate the entry list.;
	Store(const Store &);
	Store& operator=(const Store &);
	void Insert();		// Insert an entry into the directory.
	void Lookup() const;		// Look up a name in the directory.
	void Remove();		// Remove an entry.
	void Update();		// Update an existing entry.
	void DisplayDirectory() const;	// Display the current directory.
	void Save() const;              // Save directory in CVS file
	void Load();                    // Load directory from file

private:
	vector<Product*> productList;		// vector of entries
	int FindName(string aName) const;	// Return index of an entry, given a name.
};

