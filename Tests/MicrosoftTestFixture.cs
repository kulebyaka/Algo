using System;
using Models.Resource.Microsoft;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	
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
	}
}