using System;
using System.Collections.Generic;
using System.Linq;
using Models.Attributes;
using Models.Structures.Tree;

namespace Models.Resource.Microsoft
{
	public class MicrosoftTasks
	{
		// This is a DEMO task.
		// 	Write a function:
		// class Solution { public int solution(int[] A); }
		// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
		// 	For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
		// Given A = [1, 2, 3], the function should return 4.
		// Given A = [−1, −3], the function should return 1.
		// Write an efficient algorithm for the following assumptions:
		// N is an integer within the range [1..100,000];
		// each element of array A is an integer within the range [−1,000,000..1,000,000].

		public int solution1(int[] A) {
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

		// сгенерить слово. Инпут число, если четное, то одну букву повторить если нечетное то н-1 одну букву и добавить другую
		[StringTag]
		public string GenerateString(int input)
		{
			if (input % 2 == 0)
			{
				return new string('A', input);
			}

			return new string('A', input-1) + 'B';
		}
		
		// Инпут число. нужно было поделить слово на три части чтобы какая-то буква была в каждой части столько раз.
		// Ну и нужно вернуть количество таких разделений
		[StringTag]
		public int SplitTo3String(string input)
		{
			var n = input.Length;
			const char character = '0';
 
			// Calculating the total
			// number of zeros
			var characterCount = 0;
			for(int i = 0; i < n; i++)
				if (input[i] == character)
					characterCount++;
			if (characterCount % 3 != 0)
				return 0;
 
			if (characterCount == 0)
				return ((n - 1) * (n - 2)) / 2;
 
 
			// Number of zeros in each substring
			int zerosInEachSubstring = characterCount / 3;
 
			// Initialising zero to the number of ways
			// for first and second cut
			int waysOfFirstCut = 0;
			int waysOfSecondCut = 0;
 
			// Initializing the count
			int count = 0;
 
			// Traversing from the begining
			for(int i = 0; i < n; i++)
			{
         
				// Incrementing the count
				// if the element is '0'
				if (input[i] == character)
					count++;
 
				// Incrementing the ways for the
				// 1st cut if count is equal to
				// zeros required in each substring
				if (count == zerosInEachSubstring)
					waysOfFirstCut++;
 
				// Incrementing the ways for the
				// 2nd cut if count is equal to
				// 2*(zeros required in each substring)
				else if (count == 2 * zerosInEachSubstring)
					waysOfSecondCut++;
			}
 
			// Total number of ways to split is
			// multiplication of ways for the 1st
			// and 2nd cut
			return waysOfFirstCut * waysOfSecondCut;
		}
		
	}
}