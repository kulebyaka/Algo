using NetFeatures;
using NUnit.Framework;

namespace Tests
{
	[TestFixture]
	public class NetFeatures
	{
		[Test]
		public void TestMyBool()
		{
			var x = new MyBool();
			x |= true;
			x |= false;
			x |= true;
			Assert.AreEqual(x.Counter, 2);
		}
	}
}