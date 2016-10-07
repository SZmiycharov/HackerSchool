using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace segments
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) > 0 && int.Parse(input)<100000)
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

        static bool MembersInBetweenAreZeros(int[] arr, int currentIndex, int c)
        {
            bool areZero = true;
            for(int i = 0; i<=c-2; i++)
            {
                if (arr[currentIndex + 1] != 0)
                {
                    areZero = false;
                    break;
                }
                currentIndex++;
            }
            return areZero;
        }
        static void ClearUntilNextOne(ref int[] arr, int currentIndex, int n)
        {
            while(true)
            {
                if (arr[currentIndex] == 1)
                {
                    break;
                }
                else arr[currentIndex] = 1;
                
            }
        }

        static void Main(string[] args)
        {
            int n = 0;
            int a = 0;
            int b = 0;
            int c = 0;
            Console.Write("Enter a: ");
            ValidateInt(Console.ReadLine(), ref a);
            Console.Write("Enter b: ");
            ValidateInt(Console.ReadLine(), ref b);
            Console.Write("Enter c: ");
            ValidateInt(Console.ReadLine(), ref c);
            Console.Write("Enter n<length of line>: ");
            ValidateInt(Console.ReadLine(), ref n);

            int[] arr = new int [n+1];
            
            for (int i = 0; i < n + 1; i++)
            {
                if (i % a == 0) arr[i] = 1;
            }
            
            int remainder = n%b; 
            for(int i = n; i>=0; i--)
            {
                if(i % b == remainder) arr[i] = 1;
            }

            int nonRedLines = 0;
            for(int i=0; i<n+1; i++)
            {
                if(arr[i]== 1)
                {
                    for (int j = i+1; j < n+1; j++)
                    {
                        if(arr[j] == 1 && (j-i)!=c)
                        {
                            nonRedLines += j - i;
                            break;
                        }
                        if (arr[j] == 1) break;
                    }
                }
            }
            

            Console.WriteLine();
            Console.Write("Non red lines: {0}", nonRedLines);
            Console.ReadKey();
        }
    }
}
