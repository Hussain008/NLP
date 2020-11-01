import requests
import random
import sys


def minEditDistRecur(word1 , word2 , idx1 , idx2 ): 
    #if any of the words are empty then minimum cost would be the remainder characters of the other words(base case)
    if(idx1 == -1 or idx2 == -1 ):
        return max(idx1,idx2) + 1 

    #maximum integer value
    option1 = sys.maxsize

    #if both characters match then no cost option
    if(word1[idx1]==word2[idx2]):
        option1 = minEditDistRecur(word1,word2,idx1-1,idx2-1)

    option2 = minEditDistRecur(word1,word2,idx1,idx2-1) + 1 #insert
    option3 = minEditDistRecur(word1,word2,idx1-1,idx2) + 1 #remove
    option4 = minEditDistRecur(word1,word2,idx1-1,idx2-1) + 1 #replace

    current_answer = min(option1,min(option2,min(option3,option4))) 

    return current_answer






#Will help in caching values
dp={}

def minEditDistHelper(word1 , word2 , idx1 , idx2 ): 
    #if any of the words are empty then minimum cost would be the remainder characters of the other words(base case)
    if(idx1 == -1 or idx2 == -1 ):
        return max(idx1,idx2) + 1 

    #hasing the key values for dictionary
    target_key = str(idx1)+"_"+str(idx2)
    if(target_key in dp ):
        return dp[target_key]

    #maximum integer value
    option1 = sys.maxsize

    #if both characters match then no cost option
    if(word1[idx1]==word2[idx2]):
        option1 = minEditDistHelper(word1,word2,idx1-1,idx2-1)

    option2 = minEditDistHelper(word1,word2,idx1,idx2-1) + 1 #insert
    option3 = minEditDistHelper(word1,word2,idx1-1,idx2) + 1 #remove
    option4 = minEditDistHelper(word1,word2,idx1-1,idx2-1) + 1 #replace

    dp[target_key] = min(option1,min(option2,min(option3,option4))) 

    return dp[target_key]



def minEditDist(word1 , word2 ): 
    dp.clear()
    # return minEditDistRecur(word1,word2,len(word1)-1,len(word2)-1)
    return minEditDistHelper(word1,word2,len(word1)-1,len(word2)-1)


#Give it the input as a list of all potential words here 
inputText = ["laptop","watermelon","Adolf Hitler"] 


url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"



#randomly select the word
target_word = random.choice(inputText)
querystring = {"term":target_word}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "367d90020bmsh207a6d30ffb95bfp1ad928jsn454da4df8c38"
    }
#request definition from our API
response = requests.request("GET", url, headers=headers, params=querystring)

#collect the definition from out JSON object
definition = response.json()["list"][0]["definition"]


User_Guess = ""
cur_dist = -1 

while(cur_dist!=0):
    print("_____________________________________________")
    print("Guess the word by definition : \n")
    print(definition)

    User_Guess = input()
    cur_dist = minEditDist(User_Guess,target_word)

    print("Distance away from the Target word : "+str(cur_dist)+"\n\n")
    print("_____________________________________________\n\n\n\n")

print("Congratulations ! You have Guessed it correctly ! ")


