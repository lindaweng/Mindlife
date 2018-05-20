require 'pycall/import'

def getAnswer(num)
    botScript1 = ["We want to create the safest environment here at Mindlife. What can we do to make you feel safer?", "Done! I just want you to know that whatever you say here will be totally confidential. Have you ever been in counseling before?", "How long have you been going through a hard time?", "In your life now, do you feel like you have support?", "Tell me more.", "What would you like me to help you with?", "To what extent is this impacting your life?", "Why do you feel this way?", "I’m sorry to hear that.  I’ll always be there for you.", "Stay positive! On the homepage, there are some resources to help you out."]
    if (num > botScript1.length() - 1)
        return "Stay positive!"
    end
    return botScript1[num]
end

