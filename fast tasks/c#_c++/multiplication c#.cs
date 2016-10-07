using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace multiplicationFastTaskTelebid
{
    class Program
    {
        static void ValidateInt(string input, ref int number)
        {
            while (true)
            {
                if (int.TryParse(input, out number) && int.Parse(input) > 0 && int.Parse(input) < 3200000)
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

        static void Main(string[] args)
        {
            int digit = 0;
            StringBuilder helper = new StringBuilder();
            for (int i=0;i<1000000;i++)
            {
                helper = helper.Append((i * i).ToString());
            }

            Console.Write("Enter which digit from the number you want to see: ");
            ValidateInt(Console.ReadLine(), ref digit);
            
            char result = helper[digit];

            Console.Write("The {0} digit is: {1}", digit, result);


            Console.ReadKey();

        }
    }
}
