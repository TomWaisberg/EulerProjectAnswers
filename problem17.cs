using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp129
{
    class Program
    {
        public static void Main(string[] args)
        {
            int sumCharacters = 0;
            for (int i = 1; i < 1000; i++)
            {
                Console.WriteLine(NumToString(i));
                sumCharacters += NumToString(i).Length;
            }

            sumCharacters += "onethousand".Length;
            Console.WriteLine(sumCharacters);
        }

        static string NumToString(int num)
        {
            string[] digits = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
            string[] tens = { "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };

            if(num < 20)
            {
                return digits[num - 1];
            }
            else if(num < 100)
            {
                if (num % 10 == 0)
                {
                    return tens[num / 10 - 2];
                }
                else
                {
                    return tens[num / 10 - 2] + digits[num % 10 - 1];
                }
            }
            else if(num < 1000)
            {
                if(num % 100 == 0)
                {
                    return digits[num / 100 - 1] + "hundred";
                }
                else if(num % 10 == 0)
                {
                    return digits[num / 100 - 1] + "hundred" + "and" + tens[MinZero((num / 10) % 10 - 2)];
                }
                else if(num / 10 % 10 == 0)
                {
                    return digits[num / 100 - 1] + "hundred" + "and" + digits[num % 10 - 1];
                }
                else
                {
                    return digits[num / 100 - 1] + "hundred" + "and" + tens[MinZero((num / 10) % 10 - 2)] + digits[num % 10 - 1];
                }
            }
            else
            {
                return null;
            }
        }

        static int MinZero(int num)
        {
            if(num < 0)
            {
                return 0;
            }
            else
            {
                return num;
            }
        }
    }
}
