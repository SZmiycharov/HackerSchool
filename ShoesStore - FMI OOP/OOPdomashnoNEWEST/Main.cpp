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
	cout << "\n\t\t*** PHONE DIRECTORY ***";
	cout << "\n\tI \tInsert a new product into the store";   // Add new product
	cout << "\n\tL \tLook up an product";
	cout << "\n\tR \tRemove a product";	 // Delete product
	cout << "\n\tU \tUpdate a product"; //Change product
	cout << "\n\tD \tDisplay the entire store"; //Display products
	cout << "\n\tS \tSave"; //Save products
	cout << "\n\tO \tLoad"; //Load products
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
	return	((c == 'I') || (c == 'L') || (c == 'R') || (c == 'U') ||
		(c == 'D') || (c == 'S') || (c == 'O') || (c == '?') || (c == 'Q'));
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
		case 'I': d.Insert();				break;
		case 'L': d.Lookup();				break;
		case 'R': d.Remove();				break;
		case 'U': d.Update();				break;
		case 'D': d.DisplayDirectory();	    break;
		case 'S': d.Save();	                break;
		case 'O': d.Load();	                break;
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
