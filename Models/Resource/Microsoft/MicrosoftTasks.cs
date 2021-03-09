using System;
using Models.Attributes;
using Models.Structures.Tree;

namespace Models.Resource.Microsoft
{
	public class MicrosoftTasks
	{
		// From Image
		[StringTag]
		public string Compression(string input)
		{
			return "";
		}
		
		// Find nearest common root in binary search tree 
		[BinaryTreeTag]
		public int FindCommonRoot(BinaryTreeNode<int> bst, int nodeA, int nodeB)
		{
			return nodeA;
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