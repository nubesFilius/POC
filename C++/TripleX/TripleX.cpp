#include <iostream>
#include <ctime>

void gameIntroduction(int difficulty)
{
  std::cout << "\n\nYou are a secret agent breaking into a level " << difficulty;
  std::cout << " secret room.\n";
  std::cout << "Enter the correct code to continue...\n";
}

bool playGame(int difficulty)
{
  gameIntroduction(difficulty);

  int codeA = rand() % difficulty + difficulty;
  int codeB = rand() % difficulty + difficulty;
  int codeC = rand() % difficulty + difficulty;

  int codeSum = codeA + codeB + codeC;
  int codeProduct = codeA * codeB * codeC;

  std::cout << "\n+ There are 3 numbers in the code.";
  std::cout << "\n+ The codes add up to: " << codeSum;
  std::cout << "\n+ The codes multiply to give: " << codeProduct << std::endl
            << std::endl;

  int guessA, guessB, guessC;

  std::cin >> guessA >> guessB >> guessC;
  std::cout << "\nYou entered: " << guessA << guessB << guessC << std::endl;

  int guessSum = guessA + guessB + guessC;
  int guessProduct = guessA * guessB * guessC;

  std::cout << "The sum of your guesses is: " << guessSum << std::endl;
  std::cout << "The product of your guesses is: " << guessProduct << std::endl;

  if (guessSum == codeSum && guessProduct == codeProduct)
  {
    std::cout << "\nCorrect!\nYou're now moving to the next level.";
    return true;
  }
  else
  {
    std::cout << "\nIncorrect code! Please try a different combination.\n";
    return false;
  }
}

int main()
{
  srand(time(NULL));
  int levelDifficulty = 1;
  const int maxLevel = 5;
  while (levelDifficulty <= maxLevel)
  {
    bool blevelComplete = playGame(levelDifficulty);
    std::cin.clear();  // Clear errors
    std::cin.ignore(); // Discards buffer

    if (blevelComplete == true)
    {
      ++levelDifficulty;
    }
  }

  std::cout << "\n\nCongratulations! You have completed the game.\n\n";

  return 0;
}