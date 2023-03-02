from experta import *
import ast

incorrect_flag = False
ans = 'no'

def take_input(query):
    global incorrect_flag
    global ans
    if incorrect_flag:
        print("You entered a value that is neither Yes nor No.")
        incorrect_flag = False
    ans = input(query + "\nPlease type Yes/No\n")
    ans = ans.lower()
    if ans != "yes" and ans != "no":
        incorrect_flag = True
        take_input(query)
    return ans

class MedicalExpert(KnowledgeEngine):
    username = "", 

    @DefFacts()
    def needed_data(self):
        """ 
        This is a method which is called everytime engine.reset() is called.
        It acts like a constructor to this class.
        """        
        yield Fact(findDisease = 'true')
        print("Hi!\nI'm a health inference Expert Advisor, You can call me Mr. EA.\n\nYou can get yourself diagnosed here free of cost!, isn't that cool.\nI will ask you 10 questions.\n\n")
        

    @Rule(Fact(findDisease = 'true'),NOT(Fact(name=W())),salience = 1000)
    def ask_name(self):
        self.username = input("What's your name?\n")
        self.declare(Fact(name=self.username))

    @Rule(Fact(findDisease='true'), NOT (Fact(sweat = W())),salience = 995)
    def hasSweat(self):
        self.sweat = take_input("\nDo you sweat a lot?")
        self.sweat = self.sweat.lower()
        self.declare(Fact(sweat = self.sweat.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(rest = W())),salience = 985)
    def hasRest(self):
        self.rest = take_input("\nDo you experience restlessness?")
        self.rest = self.rest.lower()
        self.declare(Fact(rest = self.rest.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(moodSwings = W())),salience = 975)
    def hasMoodSwings(self):
        self.mood_swings = take_input("\nDo you experience mood swings?")
        self.mood_swings = self.mood_swings.lower()
        self.declare(Fact(moodSwings = self.mood_swings.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        self.fatigue = take_input("\nDo you experience fatigue occasionally?")
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(insomnia = W())),salience = 965)
    def hasInsomnia(self):
        self.insomnia = take_input("\nDo you experience insomnia?")
        self.insomnia = self.insomnia.lower()
        self.declare(Fact(insomnia = self.insomnia.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(suicidalThought = W())),salience = 955)
    def hasSuicidalThought(self):
        self.suicidal_thought = take_input("\nDo you usually have suicidal thought?")
        self.suicidal_thought = self.suicidal_thought.lower()
        self.declare(Fact(suicidalThought = self.suicidal_thought.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(anxiety = W())),salience = 950)
    def hasAnxiety(self):
        self.anxiety = take_input("\nDo you experience anxiety?")
        self.anxiety = self.anxiety.lower()
        self.declare(Fact(anxiety = self.anxiety.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(flashbacks = W())),salience = 945)
    def hasFlashbacks(self):
        self.flashbacks = take_input("\nDo you usually have flashbacks?")
        self.flashbacks=self.flashbacks.lower()
        self.declare(Fact(flashbacks = self.flashbacks.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(hallucinations = W())),salience = 940)
    def hasHallucinations(self):
        self.hallucinations = take_input("\nDo you experience hallucinations?")
        self.hallucinations = self.hallucinations.lower()
        self.declare(Fact(hallucinations = self.hallucinations.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(depression = W())),salience = 935)
    def hasDepression(self):
        self.depression = take_input("\nDo you experience depression?")
        self.depression = self.depression.lower()
        self.declare(Fact(depression = self.depression.strip().lower()))

   
    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'yes'),Fact(anxiety = 'no'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Factitious disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'yes'), Fact(rest = 'yes'), Fact(moodSwings = 'no'),Fact(fatigue = 'yes'),
    Fact(insomnia = 'yes'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_1(self):
        self.declare(Fact(disease = 'Anxiety disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'yes'), Fact(moodSwings = 'yes'),Fact(fatigue = 'yes'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'no'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_2(self):
        self.declare(Fact(disease = 'Bipolar disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'yes'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'yes'))
    def disease_3(self):
        self.declare(Fact(disease = 'Dissociative disorder'))


    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'yes'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_4(self):
        self.declare(Fact(disease = 'Attention Deficit Hyperactivity disorder'))


    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'yes'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'yes'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_5(self):
        self.declare(Fact(disease = 'Post-Traumatic Stress disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'yes'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'no'),Fact(flashbacks = 'no'),Fact(hallucinations='yes'),
    Fact(depression = 'yes'))
    def disease_6(self):
        self.declare(Fact(disease = 'Schizophrenia'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'yes'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='yes'),
    Fact(depression = 'yes'))
    def disease_7(self):
        self.declare(Fact(disease = 'Obsessive-Compulsive disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='yes'),
    Fact(depression = 'yes'))
    def disease_8(self):
        self.declare(Fact(disease = 'Psychotic disorder'))
    
    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'yes'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_9(self):
        self.declare(Fact(disease = 'Personality disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'yes'), Fact(rest = 'yes'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'no'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_10(self):
        self.declare(Fact(disease = 'Panic disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'no'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'yes'))
    def disease_11(self):
        self.declare(Fact(disease = 'Autism Spectrum disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'no'),
    Fact(insomnia = 'yes'),Fact(suicidalThought = 'no'),Fact(anxiety = 'yes'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'yes'))
    def disease_12(self):
        self.declare(Fact(disease = 'Impulse control and addiction disorder'))

    @Rule(Fact(findDisease='true'),Fact(sweat = 'no'), Fact(rest = 'no'), Fact(moodSwings = 'no'),Fact(fatigue = 'yes'),
    Fact(insomnia = 'yes'),Fact(suicidalThought = 'yes'),Fact(anxiety = 'no'),Fact(flashbacks = 'no'),Fact(hallucinations='no'),
    Fact(depression = 'no'))
    def disease_13(self):
        self.declare(Fact(disease = 'Depression'))


    @Rule(Fact(findDisease='true'),NOT (Fact(disease = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = 1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            mapDisease = []
            mapDisease.append('Sweating')
            mapDisease.append('Restlessness')
            mapDisease.append('Mood swings')
            mapDisease.append('Fatigue')
            mapDisease.append('Insomnia')
            mapDisease.append('Suicidal thought')
            mapDisease.append('Anxiety')
            mapDisease.append('Flashbacks')
            mapDisease.append('Hallucinations')
            mapDisease.append('Depression') 
            print('\n\nWe checked the following symptoms',mapDisease)
            mapDisease_val=[self.sweat,self.rest,self.mood_swings,self.fatigue,self.insomnia
            ,self.suicidal_thought,self.anxiety,self.flashbacks,self.hallucinations,self.depression]
            print('\n\nSymptoms in patients are :', mapDisease_val)
            
            file = open("disease_symptoms.txt", "r", encoding='utf8')
            contents = file.read().replace(u'\u2013', '-').replace(u'\u2019', '\'').replace(u'\xae', '')
            dictionary = ast.literal_eval(contents)
            file.close()
            
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'yes':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            print('\n\nYes symptoms noticed are : ', yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_symptoms:
                        count+=1
                #print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                print("No diseases found.You are healthy!")
            else:
                print("\n\nWe are unable to tell you the exact disease with confidence.But we believe that you suffer from",pred_dis)
                
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')

                print ('\n\nSome info about the disease:',pred_dis)
                
                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r", encoding='utf8')
                print(f.read().replace(u'\u2013', '-').replace(u'\u2019', '\'').replace(u'\xae', ''))
                print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r", encoding='utf8')
                print(f.read().replace(u'\u2013', '-').replace(u'\u2019', '\'').replace(u'\xae', ''))
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
        else:
            print('The most probable illness you are suffering from is:',disease)
            print('\n\n')
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('Some info about the disease:\n')
            print(disease)
            f = open("disease/disease_descriptions/" + disease + ".txt", "r", encoding='utf8')
            print(f.read().replace(u'\u2013', '-').replace(u'\u2019', '\'').replace(u'\xae', ''))
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
            f = open("disease/disease_treatments/" + disease + ".txt", "r", encoding='utf8')
            print(f.read().replace(u'\u2013', '-').replace(u'\u2019', '\'').replace(u'\xae', ''))
    # @Rule(Fact(findDisease = 'true'),
    # Fact(name=MATCH.name))
    # def greet(self, name):
    #     print("Hi!",name, "How is the weather?")
if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    # print('Printing engine facts after 1 run',engine.facts)
   