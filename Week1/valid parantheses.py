class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={")":"(" , "}":"{" , "]":"["}
        for character in s:
            if character in hashmap: #if character is a close bracket 
                if not stack: #if stack is empty
                    return False
                else:
                    top = stack.pop() #check if stack top matches close bracket and remove stack top 
                    if top!=hashmap[character]:
                        return False 
            else:
                stack.append(character) #if character is opening bracket just add it 
        return not stack #true if stack is empty, false if stack is not empty 