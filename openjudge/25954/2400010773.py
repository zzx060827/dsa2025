def __lt__(self,other):
		if isinstance(other,A):
			return self.x<other.x
		elif isinstance(other,(int,float)):
			return self.x<other
def __ge__(self,other):
	if isinstance(other,A):
		return self.x>=other.x

	