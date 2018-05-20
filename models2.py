import nltk
import re
import sys
from sys import argv
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def ajay(ans):
    ajay = SentimentIntensityAnalyzer()
    completeScore = 0
    questionWeights = [0.05, 0.20, 0.05, 0.05, 0.05, 0.20, 0.05, 0.05, 0.20, 0.10]
    print ans
    ansList = ans.split("$")
    for j in range(10):
        print ansList[j]
    for i in range(10):
        results = []
        score = 0
        count = 0
        # print (count)
        for paragraph in ansList:
            for line in paragraph:
                #Split Paragraph on basis of '.' or ? or !.
                
                for l in re.split(r"\.|\?|\!",paragraph):
                    # print(l)
                    ss = ajay.polarity_scores(l)
                    results.append(ss);
                    # print(ss['compound'])
                    score += ss['compound']
                    count += 1
            completeScore += (score/count)*questionWeights[i]
    #print(completeScore)        
    if (completeScore >= 0.1):
        return "False Alarm! You don't have Depression."
    elif (completeScore >= -0.1):
        return ("Seasonal affective disorder (SAD). This type of depression " +
                "emerges as days get shorter in the fall and winter. The mood "
                + "change may result from alterations in the body's natural daily "
                + "rhythms, in the eyes' sensitivity to light, or in how chemical "
                + "messengers like serotonin and melatonin function. The leading "
                + "treatment is light therapy, which involves daily sessions sitting "
                + "close to an especially intense light source. The usual treatments "
                + "for depression, such as psychotherapy and medication, may also be "
                + "effective.");
    elif (completeScore >= -0.4):
        return ("Persistent depressive disorder. Formerly called dysthymia, this "
                + "type of depression refers to low mood that has lasted for at least "
                + "two years but may not reach the intensity of major depression. Many "
                + "people with this type of depression type are able to function day to "
                + "but feel low or joyless much of the time. Some depressive symptoms, "
                + "such as appetite and sleep changes, low energy, low self-esteem, or "
                + "hopelessness, are usually part of the picture.")
    else:
        return  ("The classic depression type, major depression is a state where a dark "
                 + "mood is all-consuming and one loses interest in activities, even ones "
                 + "that are usually pleasurable. Symptoms of this type of depression "
                 + "include trouble sleeping, changes in appetite or weight, loss of energy, "
                 + "and feeling worthless. Thoughts of death or suicide may occur. It is "
                 + "usually treated with psychotherapy and medication. For some people with "
                 + "severe depression that isn't alleviated with psychotherapy or antidepressant "
                 + "medications, electroconvulsive therapy may be effective.")