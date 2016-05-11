#include "stdafx.h"
#include <cctype>			
#include <iostream>		
#include "ShoppingCart.h"		
#include "store.h"

using namespace std;

void ShowMenu()
// Display the main program menu.
{
	cout << "\n\t\t*** ShoppingCart ***";
	cout << "\n\tD \tDisplay all the products in the store";
	cout << "\n\tA \tAdd a new product into the shopping cart";   
	cout << "\n\tK \tDelete a product from shopping cart";	 
	cout << "\n\tS \tDisplay all the products in the shopping cart"; 
	cout << "\n\tC \tCheckout";
	cout << "\n\t? \tDisplay this menu";
	cout << "\n\tQ \tQuit"; //Quit
}

char GetAChar(char* promptString)
{
	char response;			

	cout << promptString;		
	cin >> response;			
	response = toupper(response);	
	cin.get();				
	return response;
}

char Legal(char c)
{
	return	((c == 'D') || (c == 'A') || (c == 'K') || (c == 'S') ||
		(c == 'C') || (c == '?') || (c == 'Q'));
}

char GetCommand()
{
	char cmd = GetAChar("\n\n>");	

	while (!Legal(cmd))		
	{				
		cout << "\nIllegal command, please try again . . .";
		ShowMenu();
		cmd = GetAChar("\n\n>");
	}
	return cmd;
}

int main()
{
	Store d;
	ShoppingCart s;			
	d.Load();				
	ShowMenu();				

	char command;			
	do
	{
		command = GetCommand();		
		switch (command)
		{
		case 'D': d.DisplayStore();			break;		//display all products
		case 'A': s.Insert();				break;		// add a product to shopping cart
		case 'K': s.Remove();				break;		//delete a product from shopping cart
		case 'S': s.DisplayCart();			break;		//display products in shopping cart
		case 'C': s.Checkout();	            break;		//Checkout        
		case '?': ShowMenu();				break;
		case 'Q':							break;

			
		}
	} while (command != 'Q');

	

	return 0;
}