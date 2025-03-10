using System;
using System.Threading.Tasks;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	public class TaskDelayTestFixture
	{
		[Test]
		public void TestMyAsync()
		{
			var t = Task.Run(async delegate
			{
				await Task.Delay(TimeSpan.FromSeconds(5));
				Lalalaa();
			});
			t.Wait();
			Console.WriteLine("TestMyAsync");
		}

		public async void Lalalaa()
		{
			Console.WriteLine("lalala works");
		}
	}
}