// PhoneBook.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

// Test program and general support functions
// for phone directory

#include <cctype>			// for toupper
#include <iostream>		// for cin, cout
#include "Store.h"		// for class Store

using namespace std;

void ShowMenu()
// Display the main program menu.
{
	cout << "\n\t\t*** Shoes Store ***";
	cout << "\n\tA \tAdd a new product into the store";   // Add new product
	cout << "\n\tK \tDelete a product";	 // Delete product
	cout << "\n\tC \tChange a product"; //Change product
	cout << "\n\tD \tDisplay all the products"; //Display products
	cout << "\n\tS \tSave";
	cout << "\n\tO \tLoad";
	cout << "\n\t? \tDisplay this menu";
	cout << "\n\tQ \tQuit"; //Quit
}

char GetAChar(char* promptString)
// Prompt the user and get a single character,
// discarding the Return character.
// Used in GetCommand.
{
	char response;			// the char to be returned

	cout << promptString;		// Prompt the user
	cin >> response;			// Get a char,
	response = toupper(response);	// and convert it to uppercase
	cin.get();				// Discard newline char from input.
	return response;
}

char Legal(char c)
// Determine if a particular character, c, corresponds
// to a legal menu command.  Returns 1 if legal, 0 if not.
// Used in GetCommand.
{
	return	((c == 'A') || (c == 'K') || (c == 'C') ||
		(c == 'D') || (c == 'S') || (c == 'L') || (c == '?') || (c == 'Q'));
}

char GetCommand()
// Prompts the user for a menu command until a legal 
// command character is entered.  Return the command character.
// Calls GetAChar, Legal, ShowMenu.
{
	char cmd = GetAChar("\n\n>");	// Get a command character.

	while (!Legal(cmd))		// As long as it's not a legal command,
	{				// display menu and try again.
		cout << "\nIllegal command, please try again . . .";
		ShowMenu();
		cmd = GetAChar("\n\n>");
	}
	return cmd;
}

int main()
{
	Store d;			// Create and initialize a new directory.

	ShowMenu();				// Display the menu.

	char command;			// menu command entered by user
	do
	{
		command = GetCommand();		// Retrieve a command.
		switch (command)
		{
		case 'A': d.Insert();				break;
		case 'K': d.Remove();				break;
		case 'C': d.Update();				break;
		case 'D': d.DisplayDirectory();	    break;
		case 'S': d.Save();	                break;
		case 'L': d.Load();	                break;
		case '?': ShowMenu();				break;
		case 'Q':					break;
		}
	} while (command != 'Q');

	Store d1 = d;
	d1.DisplayDirectory();

	Store d2;

	d2 = d1;
	d2.DisplayDirectory();

	return 0;
}
