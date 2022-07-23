using Models.Attributes;

namespace Models.Resource.Microsoft
{
	public class MicrosofrVitaly
	{
		// сгенерить слово. Инпут число, если четное, то одну букву повторить если нечетное то н-1 одну букву и добавить другую
		[Tag(new[] {Tags.String})]
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
		[Tag(new[] {Tags.String})]
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
 
			// Traversing from the beginning
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