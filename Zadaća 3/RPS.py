from RPSError import RPSError

class RPS():
	def __init__(self):
		self.playerOneNum = -1
		self.playerOneInput = None
		self.playerTwoNum = -1
		self.playerTwoInput = None
	
	def StringToNum(self, playerString = ""):
		output = -1
		
		if(playerString == "rock"):
			output = 0
		elif(playerString == "paper"):
			output = 1
		elif(playerString == "scissors"):
			output = 2
		else:
			output = -1
			raise RPSError(101)
		
		return output
			
	def Play(self):
		print("\n")
		self.playerOneInput = input("Player 1 Choice (Rock/Paper/Scissors): ").lower()
		self.playerOneNum = self.StringToNum(self.playerOneInput)

		self.playerTwoInput = input("Player 2 Choice (Rock/Paper/Scissors): ").lower()
		self.playerTwoNum = self.StringToNum(self.playerTwoInput)

		remainder = (self.playerOneNum - self.playerTwoNum) % 3

		if(remainder == 0):
			winner = "Nobody. It's a tie!"
		elif(remainder == 1):
			winner = "Player 1"
		elif(remainder == 2):
			winner = "Player 2"
		
		print("~" * 50)
		print("Player 1 has chosen: {}".format(self.playerOneInput.capitalize()))
		print("Player 2 has chosen: {}".format(self.playerTwoInput.capitalize()))
		print("~" * 50)

		print("The winner is: {}".format(winner) + "\n")

if __name__ == "__main__":
	game = RPS()
	game.Play()