using System;

namespace NetFeatures
{
	public class MyBool : IEquatable<MyBool>
	{
		public bool Equals(MyBool other)
		{
			if (ReferenceEquals(null, other))
				return false;
			if (ReferenceEquals(this, other))
				return true;
			return _value == other._value && Counter == other.Counter;
		}

		public override bool Equals(object obj)
		{
			if (ReferenceEquals(null, obj))
				return false;
			if (ReferenceEquals(this, obj))
				return true;
			if (obj.GetType() != this.GetType())
				return false;
			return Equals((MyBool) obj);
		}

		public override int GetHashCode()
		{
			return HashCode.Combine(_value, Counter);
		}

		private readonly bool _value;
		public int Counter { get; private set; }

		public MyBool(bool b)
		{
			_value = b;
		}
		
		public MyBool()
		{
			_value = false;
		}

		public static bool operator ==(MyBool a, bool b)
		{
			if (a == null)
			{
				return false;
			}

			return a._value == b;
		}

		public static bool operator !=(MyBool a, bool b)
		{
			return !(a == b);
		}

		public static explicit operator MyBool(bool b) => new MyBool(b);

		public static MyBool operator |(MyBool a, bool b)
		{
			bool x = b || a._value;
			if (b)
				a.Counter++;
			return a;
		}
	}
}

