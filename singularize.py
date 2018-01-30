#Written by Lam Ngo
#My naive implementation of singularing an english word.

#abnormal plural to singular. Collected from the Internet.
notreg = {
     'appendices':'appendix',
     'barracks':'barracks',
     'cacti':'cactus',
     'children':'child',
     'criteria':'criterion',
     'deer':'deer',
     'echoes':'echo',
     'elves':'elf',
     'embargoes':'embargo',
     'foci':'focus',
     'fungi':'fungus',
     'geese':'goose',
     'heroes':'hero',
     'hooves':'hoof',
     'indices':'index',
     'knives':'knife',
     'leaves':'leaf',
     'lives':'life',
     'men':'man',
     'mice':'mouse',
     'nuclei':'nucleus',
     'people':'person',
     'phenomena':'phenomenon',
     'potatoes':'potato',
     'selves':'self',
     'syllabi':'syllabus',
     'tomatoes':'tomato',
     'torpedoes':'torpedo',
     'vetoes':'veto',
     'women':'woman'
    }

vowels = 'aeiou'
consonants = "bcdfghjklmnpqrstvwxyz"
special_ending_1 = 'sxz'
special_ending_2 = 'chsh'

#This is a very naive implementation
def convert(word):
    #GLOBAL VARIABLE IS EVIL
    global notreg

    #check to see if the word exists in the dictionary
    result = notreg.get(word)
    if result:
        return result

    if len(word) > 3:
        #end with 'ies' and root ends with a consonant then change ies to y
        if word[-3:] == 'ies' and consonants.find(word[-4:-3]) != -1:
            return word[:-3] + 'y'
        if word[-2:] == 'es':
            #ends with 'es' and root ends with ch or sh
            if special_ending_1.find(word[-3:-2]) != -1 or special_ending_2.find(word[-4:-2]) != -1:
                return word[:-2]
            #ends with 'es' and root ends with s,x or z
            elif consonants.find(word[-4:-3]) != -1 and word[-3:-2] == 'o':
                return word[:-2]
        #else: just remove the s
        if word[-1:] == 's':
            return word[:-1]
    #if none of the above is the case, it is likely that the word is not plural,
    #hence, return None
    return None
