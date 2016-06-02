using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace straweberries
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) > 0 && int.Parse(input) < 100000)
                {
                    number = int.Parse(input);
                    break;
                }
                else
                {
                    Console.Write("Bad input! Try again: ");
                    input = Console.ReadLine();
                }
            }
        }

        static void MakeNeighborsBadStrawberries(ref int [,] arr, int arri, int arrj, int day, int indexi, int indexj)
        {
            //idnexi, indexj - index of the bad strawberry
            if (indexi - 1 != -1 && arr[indexi - 1, indexj] != 1 && arr[indexi - 1, indexj] != day-1)
            {
                arr[indexi - 1, indexj] = day;
            }
            if (indexj - 1 != -1 && arr[indexi, indexj - 1] != 1 && arr[indexi, indexj - 1] != day - 1)
            {
                arr[indexi, indexj - 1] = day;
            }
            if (indexj + 1 != arrj && arr[indexi, indexj + 1] != 1 && arr[indexi, indexj + 1] != day-1)
            {
                arr[indexi, indexj + 1] = day;
            }
            if (indexi + 1 != arri && arr[indexi + 1, indexj] != 1 && arr[indexi + 1, indexj] != day - 1)
            {
                arr[indexi + 1, indexj] = day;
            }
        }

        static void Main(string[] args)
        {
            int K = 0, L = 0, i1 = 0, i2 = -1, j1 = 0, j2 = 0;
            string choice;
            Console.Write("Enter K: ");
            ValidateInt(Console.ReadLine(), ref K);
            Console.Write("Enter L: ");
            ValidateInt(Console.ReadLine(), ref L);
            Console.Write("Enter i1: ");
            ValidateInt(Console.ReadLine(), ref i1);
            Console.Write("Enter j1: ");
            ValidateInt(Console.ReadLine(), ref j1);
            Console.Write("Enter another one? <y or n>");
            choice = Console.ReadLine();
            if(choice =="y") 
            {
                Console.Write("Enter i2: ");
                ValidateInt(Console.ReadLine(), ref i2);
                Console.Write("Enter j2: ");
                ValidateInt(Console.ReadLine(), ref j2);
            }

            
            int[,] arr = new int[8, 10] { { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }, 
                                          { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                                          { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }};

            arr[i1, j1] = 1;
            if (i2 != -1) arr[i2, j2] = 1;

            int day = 2;

            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i1, j1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i2, j2);
            day++;
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i1 - 1, j1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i1, j1 -1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i1, j1 + 1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i1 + 1, j1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i2 - 1, j2);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i2, j2 - 1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i2, j2 + 1);
            MakeNeighborsBadStrawberries(ref arr, 8, 10, day, i2 + 1, j2);

            for (int p = 0; p < 8; p++)
            {
                for(int q = 0; q<10; q++)
                {
                    Console.Write("{0}  ", arr[p, q]);
                }
                Console.WriteLine();
            }

            Console.ReadKey();
        }
    }
}
