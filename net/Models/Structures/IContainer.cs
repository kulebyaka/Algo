namespace Models.Structures
{
	public interface IContainer<T> where T : struct
	{
		public T Value { get; set; }
	}
}
