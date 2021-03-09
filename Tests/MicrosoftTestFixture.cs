using System;
using System.Collections.Generic;
using Models.Resource.Microsoft;
using Models.Structures.Tree;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	[Parallelizable(ParallelScope.All)]
	public class MicrosoftTestFixture
	{
		[Test]
		[TestCase(10d, 0.1)]
		public void SqrtTest(double variable, double eps)
		{
			var microsoftTasks = new MicrosoftTasks();
			double mySqrt = microsoftTasks.Sqrt(variable, eps);
			double actualSqrt = Math.Sqrt(variable);
			Assert.True(Math.Abs(mySqrt - actualSqrt) < eps);
		} 
		
		[Test, TestCaseSource(nameof(AddInputNearestCommonNode))]
		public void NearestCommonNodeTest(int?[] bst, int a, int b, int expectedCommonRoot)
		{
			var microsoftTasks = new MicrosoftTasks();
			var commonRoot = microsoftTasks.FindCommonRoot(new BinaryTreeNode<int>(bst), a, b);
			Assert.AreEqual(commonRoot, expectedCommonRoot);
		} 
		
		// TestCaseData
		private static IEnumerable<TestCaseData> AddInputNearestCommonNode()
		{
			yield return new TestCaseData( new int?[]{5, 3, 8, 1, 4, null, 10}, 4, 8, 5);
		}
	}
	
}