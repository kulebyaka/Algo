namespace Models.Structures.Tree
{
	public class BinaryTreeNode<T>:IContainer<T> where T : struct
	{
		public BinaryTreeNode(T?[] values) : this(values, 0) {}

		BinaryTreeNode(T?[] values, int index)
		{
			Load(this, values, index);
		}

		void Load(BinaryTreeNode<T> tree, T?[] values, int index)
		{
			if (values[index] == null)
			{
				return;
			}
			Value = (T) values[index];
			int i = index * 2 + 1;
			if (i < values.Length)
			{
				tree.Left = values[i] == null ? null :  new BinaryTreeNode<T>(values, i);
			}
			if (i+1 < values.Length)
			{
				tree.Right = values[i+1] == null ? null : new BinaryTreeNode<T>(values, i+1);
			}
		}

		public T Value { get; set; }
		public BinaryTreeNode<T> Left { get; set; }
		public BinaryTreeNode<T> Right{ get; set; }
	}
}