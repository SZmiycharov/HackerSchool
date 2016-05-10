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
	void Insert();		// Insert an entry into the directory.
	void Lookup() const;		// Look up a name in the directory.
	void Remove();		// Remove an entry.
	void Update();		// Update an existing entry.
	void DisplayDirectory() const;	// Display the current directory.
	void Save() const;              // Save directory in CVS file
	void Load();                    // Load directory from file
private:
	int	maxSize,		// the maximum allowable number of entries
		currentSize;		// the current number of entries
	Product** productList;		// pointer to the list of entries
	void Grow();
	int FindName(string aSKU) const;	// Return index of an entry, given a name.
};
