# Chapter 1
- Table 1.1 is a summary of nontechnical aspects to interviewing
- Table 1.2 is a study guide depending on how much time to study
- Resume tips (page 10)
- Table 1.3 has data structures and their key points
- Table 1.4 has algorithms and their key points
- Table 1.5 has logical principals and their key points

# Chapter 2
- Approaching the interview problem (page 15)
- Presenting the solution (page 16)
- Know interviewers and company. List of company and examples on who they want to hire (page 18)
- Negotiating an offer (page 20)

# Chapter 4
- In python, everything is an object - including Booleans, integers, characters, etc.
- Integers in python are unbounded
- ```sys.maxsize``` can be used to find word size
- Bounds on floats are specified in ```sys.float_info```
- Table 4.1 has top tips for primitive types
- Negative numbers in python are treated as 2's complement value. No concept of an unsigned shift in Python since integers have infinite precision
- Floats are not infinite precision like integers are
- use ```math.isclose()``` to compare float values
- **Commit to memory** bit-fiddling trick ```x&(x-1)``` = x with its lowest set bit erased
    - If x = (00101100) then x-1 = (00101011), so x&(x-1) = (00101100)&(00101011) = (00101000)
- Another key bit-fiddling trick is x & ~(x - 1) isolates the lowest bit that is 1 in x
- ~ is the bitwise complement operator