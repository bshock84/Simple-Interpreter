#Token types
#
#EOF (end-of-file) token is used to indicate that 
#there is no more input left for lexical analysis	
#initialises the variables INTEGER, PLUS, AND EOF equal to INTEGER, PLUS, AND EOF.
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


	
	
class Token(object):
	
	def __init__(self, type, value):
		# token type: INTEGER, PLUS, or EOF
		self.type = type
		#toekn value: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', or None
		self.value = value
		
	def __str__(self):
		"""String representation of the class instance.
		
		Examples:
			Token(INTEGER, 3)
			Token(PLUS '+')
		"""
			#returns a string of Token(type, value)
		return 'Token({type}, {value})'.format(
			type=self.type, 
			value=repr(self.value)
		)
		
		def __repr__(self):
			return self.__str__()
			
class Interpreter(object):
		
	def __init__(self, text):
		# client string input, e.g. "3+5"
		self.text = text
		#self.pos is an index into self.text
		self.pos = 0
		#current token instance
		self.current_token = None
		
	def error(self):
		raise Exception('Error parsing input')
		
	def get_next_token(self):
		"""Lexical analyzer (also known as scanner or tokenizer)
		
		This method is responsible for breaking a sentence
		apart into tokens.  One token at a time.
		"""
		
		text = self.text
		
		#is self.pos index past the end of the self.text?
		#if so, then return EOF token because there is no more
		#input left to convert into tokens
		
			#If the pos is higher than the length of the string then it sets the token to end of file.
		if self.pos > len(text) -1:
			return Token(EOF, None)
			
		#get a character at the position self.pos and decide
		#what token to create based on the single character
				
				#gets the character at the pos index of the inputted string
		current_char = text[self.pos]
		
		# if the character is a digit then convert it to 
		# integer, create an INTEGER token, increment self.pos
		# index to point to the next character after the digit, 
		# and return the INTEGER token
		if current_char.isdigit():
			token = Token(INTEGER, int(current_char))
			self.pos += 1
			return token
			
		if current_char == '+':
			token = Token(PLUS, current_char)
			self.pos += 1
			return token
			
		self.error()
		
	def eat(self, token_type):
	# compare the current token type with the passed token
	# type and if they match then "eat" the current token
	# and assign the next token to the self.current_token,
	# otherwise raise an exception.
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()
	
	def expr(self):
		"""expr -> INTEGER PLUS INTEGER"""

		#set current token to the first token taken from the input
		self.current_token = self.get_next_token()
				
		left = 0
		op = ''
		right = 0
		operator_found = False

		while self.current_token.type != 'EOF':
			if operator_found == False:
				if self.current_token.type == 'INTEGER':
					left = int(str(left) + str(self.current_token.value))
					self.eat(INTEGER)
				elif self.current_token.type == 'PLUS':
					op = self.current_token.value
					operator_found = True
					self.eat(PLUS)
			elif operator_found == True:
				if self.current_token.type == 'INTEGER':
					right = int(str(right) + str(self.current_token.value))
					self.eat(INTEGER)
	
		result = left + right
		return result
		
def main():
	while True:
		try:
			text = raw_input('calc>')
		except EOFError:
			break
		if not text:
			continue
		interpreter = Interpreter(text)
		result = interpreter.expr()
		print "The result is", result
		
		
if __name__ == '__main__':
	main()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		