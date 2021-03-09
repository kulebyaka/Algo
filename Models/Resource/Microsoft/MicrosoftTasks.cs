using System;
using Models.Attributes;

namespace Models.Resource.Microsoft
{
	public class MicrosoftTasks
	{
		// From Image
		[StringTag]
		public static string Compression(string input)
		{
			return "";
		}
		// Find the square root of a number without using the sqrt method
		[MathTag]
		public double Sqrt(double variable, double epsilon = 0.1)
		{
			double found = 0.1;
			while (Math.Abs((found*found - variable)) > epsilon)
			{
				if (found * found > variable)
				{
					found = found - found / 2;
				}
				else
				{
					found = found + found / 2;
				}
			}
			return found;
		}
	}
}