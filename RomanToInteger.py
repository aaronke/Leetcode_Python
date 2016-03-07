def romanToInt(self, s):
	numsrals={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
	sum=0;
	s=s[::-1]
	last=None
	for x in s:
		if last and numsrals[x]<last:
			sum-=2*numsrals[x]
		sum+=numsrals[x]
		last=numsrals[x]
	return sum