using System;
using System.Collections.Generic;
using System.Linq;
using Models.Attributes;
using Models.Structures.Tree;

namespace Models.Resource.Microsoft
{
	public class MicrosoftTasks
	{
		/// <summary>
		/// This is a DEMO task.
		/// Write a function:
		/// class Solution { public int Task1(int[] A); }
		/// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
		/// 	For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
		/// Given A = [1, 2, 3], the function should return 4.
		/// Given A = [−1, −3], the function should return 1.
		/// Write an efficient algorithm for the following assumptions:
		/// N is an integer within the range [1..100,000];
		/// each element of array A is an integer within the range [−1,000,000..1,000,000].
		/// </summary>
		/// <param name="A">N integers</param>
		/// <returns>the smallest positive integer (greater than 0) that does not occur in A</returns>
		public int FindSmallestNotOccuringInteger(int[] A) {
			// write your code in C# 6.0 with .NET 4.5 (Mono)

			var n = A.Length;
			var set = new HashSet<int>();
			foreach (var a in A) {
				if (a > 0) {
					set.Add(a);
				}
			}
			for (int i = 1; i <= n + 1; i++) {
				if (!set.Contains(i)) {
					return i;
				}
			}

			return n + 1;
		}
		
		/// <summary>
		/// Get max count of even pairs on the circle
		/// </summary>
		/// <see href="file:../Description/Task2.jpg">Task screen</see>
		/// <param name="A">array of integers</param>
		/// <returns></returns>
		[Tag( new []{Tags.String})]
		public string Compression(string input)
		{
			return "";
		}
		
		// Find nearest common root in binary search tree 
		[Tag(new[] {Tags.Tree, Tags.BinaryTree})]
		public static BinaryTreeNode<int> FindCommonRoot(BinaryTreeNode<int> bstRoot, int nodeA, int nodeB)
		{
			return null;
		}
		
		// Find the square root of a number without using the sqrt method
		[Tag(new[] {Tags.Math})]
		public static double Sqrt(double variable, double epsilon = 0.1)
		{
			double found = 0.1;
			while (Math.Abs((found*found - variable)) > epsilon)
			{
				if (found * found > variable)
				{
					found -= found / 2;
				}
				else
				{
					found += found / 2;
				}
			}
			return found;
		}
	}
}